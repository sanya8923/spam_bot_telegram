from aiogram.types import Message


class MessageChecker:
    def __init__(self, message: Message):
        self.message = message

    async def url_check(self):
        print(f'url_check')
        pass

    async def flood_check(self):
        print(f'flood_check')
        pass

    async def ban_words_check(self):
        print('ban_words_check')
        pass

