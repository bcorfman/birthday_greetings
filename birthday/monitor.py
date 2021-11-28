import os
import asyncio
import datetime
import repo


class BirthdayMonitor:
    def __init__(self):
        birthday_file = os.path.join('data', 'birthdays.txt')
        self.repo = repo.FileRepository(birthday_file)

    async def event_loop(self):
        while True:

            await asyncio.sleep(1)


async def main():
    # logging.basicConfig(filename='debug.txt', filemode='w', encoding='utf-8', level=logging.DEBUG)
    monitor = BirthdayMonitor()
    await monitor.event_loop()


if __name__ == '__main__':
    asyncio.run(main())
