from object_manager.object_manager import ObjManager
from aiogram.types import Message
from message_checker.message_checker import MessageChecker


class MessageManager(ObjManager):
    def __init__(self, message: Message):
        self.message = message

    async def check(self):
        print('check in MessageManager')
        checker = MessageChecker(self.message)
        return 0
