from birthday.repo import FileRepository, SqliteRepository


def test_read_file_repository():
    file_repo = FileRepository()
    record = file_repo.records.pop()
    assert record.last_name == 'Corfman'
    assert record.first_name == 'Doris'
    assert record.year == 1969
    assert record.month == 11
    assert record.day == 7
    assert record.email == 'devoncecil@fastmail.fm'


def test_read_sqlite_repository():
    sqlite_repo = SqliteRepository()
    record = sqlite_repo.records.pop()
    assert record.last_name == 'Corfman'
    assert record.first_name == 'Doris'
    assert record.year == 1969
    assert record.month == 11
    assert record.day == 7
    assert record.email == 'devoncecil@fastmail.fm'
