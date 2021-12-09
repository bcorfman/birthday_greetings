import pytest
import datetime
from birthday.monitor import BirthdayMonitor
from birthday.messenger import EmailService
from birthday.repo import Repository
from birthday.mail import MailhogSMTP
from birthday.friend import Friend


class FakeRepository(Repository):
    def __init__(self, filename=''):
        self.filename = filename
        self.records = []
        self.read()

    def read(self):
        records = [['Doe', 'John', '1951/01/03', 'aardvark@foo.com', None],
                   ['Doe', 'Jane', '1984/07/08', 'msaardvark@foo.com', '2020-07-08'],
                   ['Banner', 'Bruce', '1971/12/21', 'mrgreen@zone.com', '2019-07-08']]
        for record in records:
            self.records.append(Friend(*record))


@pytest.mark.freeze_time('2022-01-03')
@pytest.mark.asyncio
async def test_monitor_john_doe_birthday_message():
    result = False
    repo = FakeRepository()
    monitor = BirthdayMonitor(repo, EmailService())
    is_logged_in = await monitor.service_login(MailhogSMTP)
    if is_logged_in:
        result = await monitor.handle_birthday_messages()
    assert result is True
    count = 0
    for record in repo.records:
        if record.first_name == 'John' and record.last_name == 'Doe':
            count += 1
            assert record.greeting_sent == datetime.date.today()
    assert count == 1


@pytest.mark.freeze_time('2022-07-08')
@pytest.mark.asyncio
async def test_monitor_jane_doe_birthday_message():
    result = False
    repo = FakeRepository()
    monitor = BirthdayMonitor(repo, EmailService())
    is_logged_in = await monitor.service_login(MailhogSMTP)
    if is_logged_in:
        result = await monitor.handle_birthday_messages()
    assert result is True
    count = 0
    for record in repo.records:
        if record.first_name == 'Jane' and record.last_name == 'Doe':
            count += 1
            assert record.greeting_sent == datetime.date.today()
    assert count == 1


@pytest.mark.freeze_time('2022-12-21')
@pytest.mark.asyncio
async def test_monitor_bruce_banner_birthday_message():
    result = False
    repo = FakeRepository()
    monitor = BirthdayMonitor(repo, EmailService())
    is_logged_in = await monitor.service_login(MailhogSMTP)
    if is_logged_in:
        result = await monitor.handle_birthday_messages()
    assert result is True
    count = 0
    for record in repo.records:
        if record.first_name == 'Bruce' and record.last_name == 'Banner':
            count += 1
            assert record.greeting_sent == datetime.date.today()
    assert count == 1
