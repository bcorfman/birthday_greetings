import pytest
from birthday.messenger import SMSMessenger, EmailMessenger


@pytest.mark.asyncio
async def test_sms():
    messenger = SMSMessenger()
    result = await messenger.send_birthday_greeting()
    assert result is True


@pytest.mark.asyncio
async def test_email():
    messenger = EmailMessenger()
    result = await messenger.send_birthday_greeting()
    assert result is True
