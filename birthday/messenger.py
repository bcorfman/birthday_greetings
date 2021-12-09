import os
import logging
import asyncio
from abc import ABC, abstractmethod
from smtplib import SMTPHeloError, SMTPAuthenticationError, SMTPNotSupportedError, SMTPException, \
    SMTPRecipientsRefused, SMTPSenderRefused, SMTPDataError, SMTPServerDisconnected, SMTPConnectError


class MessengerService(ABC):
    def __init__(self):
        self.smtp = None

    @abstractmethod
    async def login_to_server(self, client, username, password, tries_allowed):
        return NotImplementedError

    @abstractmethod
    async def send_birthday_greeting(self, record, sender, tries_allowed):
        return NotImplementedError


class EmailService(MessengerService):
    def __init__(self):
        super().__init__()

    async def login_to_server(self, client_session, username, password, tries_allowed=3):
        is_logged_in = False
        login_tries = 0
        retry_time = 1
        while not is_logged_in:
            try:
                self.smtp = client_session(username, password)
                is_logged_in = True
            except (SMTPConnectError, SMTPHeloError, SMTPAuthenticationError, SMTPNotSupportedError,
                    SMTPException) as err:
                logging.error(f'SMTP login: {err}')
                login_tries += 1
            if is_logged_in or login_tries > tries_allowed:
                break
            await asyncio.sleep(retry_time)
            retry_time *= 2  # double the wait time after each retry
        return is_logged_in

    async def send_birthday_greeting(self, record, sender=os.environ['BIRTHDAY_MAIL_SENDER'], tries_allowed=3):
        is_sent = False
        number_of_tries = 0
        retry_time = 1
        while not is_sent:
            try:
                self.smtp.send_email(sender, record.email, 'Happy birthday!', f'Happy birthday, {record.first_name}!')
                is_sent = True
            except (SMTPHeloError, SMTPServerDisconnected, SMTPRecipientsRefused, SMTPSenderRefused, SMTPDataError,
                    SMTPNotSupportedError, SMTPException) as err:
                logging.error(f'SMTP send_message: {err}')
                number_of_tries += 1
            if is_sent or number_of_tries > tries_allowed:
                break
            await asyncio.sleep(retry_time)
            retry_time *= 2  # double the wait time after each retry
        return is_sent
