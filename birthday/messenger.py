class Messenger:
    async def send_birthday_greeting(self):
        return False


class SMSMessenger(Messenger):
    pass


class EmailMessenger(Messenger):
    pass
