from object_manager.object_manager import ObjManager
from aiogram.types import Message
from checkers.message_checker import MessageChecker
from member_manager import MemberManager
from checkers.new_member_message_checker import NewMemberChecker
from checkers.middle_member_message_checker import MiddleMemberChecker


class MessageManager(ObjManager):
    def __init__(self, message: Message):
        self.message = message

    async def check(self):
        print('check in MessageManager')
        member = self.message.from_user
        member_manager = MemberManager(member)
        member_status = await member_manager.get_status_member()
        message_checker = MessageChecker(self.message)

        if member_status == 'new_member':
            new_member_checker = NewMemberChecker()
        else:
            pass

        return 0
