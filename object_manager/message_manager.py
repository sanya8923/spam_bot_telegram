from object_manager.object_manager import ObjManager
from aiogram.types import Message


class MessageManager(ObjManager):
    def __init__(self, message: Message):
        self.message = message

    async def check(self):
        print('check in MessageManager')
        url = self.message
        return 0
