from object_manager.object_manager import ObjManager
from aiogram.types import Message
from member_manager import MemberManager
from checkers.new_member_message_checker import NewMemberMessageChecker
from checkers.middle_member_message_checker import MiddleMemberMassageChecker


class MessageManager(ObjManager):
    def __init__(self, message: Message):
        self.message = message
        self.member = self.message.from_user

    async def check(self):
        print('check in MessageManager')
        member_manager = MemberManager(self.member)
        member_status = await member_manager.get_status_member()
        try:
            if member_status == 'new_member':
                message_checker = NewMemberMessageChecker(self.message)
                if await message_checker.url_check() or \
                        await message_checker.ban_words_check() or \
                        await message_checker.flood_check():
                    return True
                else:
                    return False
            else:
                message_checker = MiddleMemberMassageChecker(self.message)
                if await message_checker.url_check() or \
                        await message_checker.ban_words_check() or \
                        await message_checker.flood_check():
                    return True
                else:
                    return False
        except (ValueError, TypeError) as e:
            raise (ValueError, TypeError)
