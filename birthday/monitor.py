import os
import logging
import asyncio
import datetime
from smtplib import SMTPException
from dateutil.relativedelta import relativedelta
from birthday.repo import FileRepository
from birthday.messenger import EmailService
from birthday.mail import FastMailSMTP


def greeting_already_sent_this_year(record):
    return record.greeting_sent is not None and record.greeting_sent + relativedelta(years=1) > datetime.date.today()


class BirthdayMonitor:
    def __init__(self, repository, messenger):
        self.repo = repository
        self.messenger = messenger
        self.exit_flag = False

    async def service_login(self, service=FastMailSMTP):
        logged_in = await self.messenger.login_to_server(service, os.environ['BIRTHDAY_MAIL_USERNAME'],
                                                         os.environ['BIRTHDAY_MAIL_PASSWORD'])
        if not logged_in:
            raise SMTPException("Monitor failed to start. Check log for details.")
        return True

    async def handle_birthday_messages(self):
        message_sent = False
        while True:
            today = datetime.date.today()
            for record in self.repo.records:
                if record.month == today.month and record.day == today.day and \
                        not greeting_already_sent_this_year(record):
                    result = await self.messenger.send_birthday_greeting(record)
                    if result:
                        record.greeting_sent = today
                        message_sent = True
            if self.exit_flag or message_sent:
                break
            await asyncio.sleep(10)
        return True


async def main():
    monitor = BirthdayMonitor(FileRepository(), EmailService())
    await monitor.service_login()
    result = True
    while result:
        result = await monitor.handle_birthday_messages()


if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', level=logging.ERROR, filemode='w')
    asyncio.run(main())
