from aiogram.types import Message


class MessageChecker:
    def __init__(self, message: Message):
        self.message = message

    async def url_check(self):
        pass

    async def flood_check(self):
        pass
