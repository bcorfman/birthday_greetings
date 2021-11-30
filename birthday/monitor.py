import os
import asyncio
import datetime
import repo
import messenger


class BirthdayMonitor:
    def __init__(self):
        birthday_file = os.path.join('data', 'birthdays.txt')
        self.repo = repo.FileRepository(birthday_file)
        self.messenger = messenger.EmailMessenger()
        self.exit_flag = False

    async def event_loop(self):
        while True:
            today = datetime.date.today()
            for record in self.repo.records:
                if record.year == today.year and record.month == today.month and record.day == today.day:
                    messenger.send_birthday_greeting(record)
                    record.greeting_sent = today
            if self.exit_flag:
                break
            await asyncio.sleep(1)


async def main():
    # logging.basicConfig(filename='debug.txt', filemode='w', encoding='utf-8', level=logging.DEBUG)
    monitor = BirthdayMonitor()
    await monitor.event_loop()


if __name__ == '__main__':
    asyncio.run(main())
