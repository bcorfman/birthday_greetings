import pytest
import os
from datetime import date
from birthday.messenger import EmailService
from birthday.mail import MailhogSMTP
from birthday.friend import Friend


@pytest.mark.asyncio
async def test_email():
    messenger = EmailService()
    result = await messenger.login_to_server(MailhogSMTP, os.environ['BIRTHDAY_MAIL_USERNAME'],
                                             os.environ['BIRTHDAY_MAIL_PASSWORD'])
    assert result is True
    result = await messenger.send_birthday_greeting(Friend('Brandon', 'Corfman', '1933/10/01',
                                                           'bcorfman1@gmail.com'))
    assert result is True
