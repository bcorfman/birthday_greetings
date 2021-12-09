import os
import sqlite3
import contextlib
from abc import ABC, abstractmethod
from birthday.friend import Friend


class Repository(ABC):
    @abstractmethod
    def read(self):
        raise NotImplementedError


class FileRepository(Repository):
    def __init__(self, filename=''):
        self.filename = filename or os.path.join('data', 'birthdays.txt')
        self.records = []
        self.read()

    def read(self):
        with open(self.filename) as f:
            header = f.readline().strip()

            for line in f.readlines():
                elements = line.strip().replace(',', '').split()
                self.records.append(Friend(*elements))


class SqliteRepository(Repository):
    def __init__(self, filename=''):
        self.filename = filename or os.path.join('data', 'birthdays.db')
        self.records = []
        self.read()

    def read(self):
        with contextlib.closing(sqlite3.connect(self.filename)) as conn:
            with contextlib.closing(conn.cursor()) as cursor:  # auto-closes
                header = ', '.join([field[1] for field
                                    in [row for row in
                                        cursor.execute("SELECT * from pragma_table_info('Birthdays') as tblInfo")
                                   .fetchall()]])

                for elements in cursor.execute('SELECT * FROM birthdays'):
                    self.records.append(Friend(*elements))
