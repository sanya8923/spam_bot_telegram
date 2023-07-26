from object_manager.object_manager import ObjManager
from aiogram.types import Message
from message_checker.message_checker import MessageChecker
from member_manager import MemberManager


class MessageManager(ObjManager):
    def __init__(self, message: Message):
        self.message = message

    async def check(self):
        print('check in MessageManager')
        member = self.message.from_user
        member_manager = MemberManager(member)
        member_status = await member_manager.get_status_member()

        checker = MessageChecker(self.message)
        return 0
