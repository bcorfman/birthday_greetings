from birthday.repo import FileRepository, SqliteRepository


def test_read_file_repository():
    file_repo = FileRepository()
    record = file_repo.records.pop()
    assert record.last_name == 'Doe'
    assert record.first_name == 'Jane'
    assert record.year == 1969
    assert record.month == 7
    assert record.day == 8
    assert record.email == 'jane.doe@zone.com'


def test_read_sqlite_repository():
    sqlite_repo = SqliteRepository()
    record = sqlite_repo.records.pop()
    assert record.last_name == 'Doe'
    assert record.first_name == 'Jane'
    assert record.year == 1969
    assert record.month == 7
    assert record.day == 8
    assert record.email == 'jane.doe@zone.com'
