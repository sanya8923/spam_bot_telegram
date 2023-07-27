from aiogram.types import Message


class MessageChecker:
    def __init__(self, message: Message):
        self.message = message

    async def url_check(self) -> bool:
        print(f'url_check')
        return True

    async def flood_check(self) -> bool:
        print(f'flood_check')
        return True

    async def ban_words_check(self) -> bool:
        print('ban_words_check')
        return True

