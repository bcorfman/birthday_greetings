from dataclasses import dataclass
from dateutil import parser
from typing import Union
import datetime


@dataclass
class Friend:
    last_name: str
    first_name: str
    date_of_birth: datetime.date
    email: str
    greeting_sent: Union[datetime.date, None]

    def __init__(self, *args):
        self.last_name = args[0]
        self.first_name = args[1]
        self.date_of_birth = parser.parse(args[2])
        self.email = args[3]
        if len(args) == 5 and args[4] is not None:
            self.greeting_sent = parser.parse(args[4])
        else:
            self.greeting_sent = None

    @property
    def year(self):
        return self.date_of_birth.year

    @property
    def month(self):
        return self.date_of_birth.month

    @property
    def day(self):
        return self.date_of_birth.day

