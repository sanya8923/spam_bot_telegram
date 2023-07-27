from object_manager.object_manager import ObjManager
from aiogram.types import Message
from object_manager.member_manager import MemberManager
from checkers.new_member_message_checker import NewMemberMessageChecker
from checkers.middle_member_message_checker import MiddleMemberMassageChecker
from checkers.admin_message_checker import AdminMessageChecker
from checkers.creator_message_checker import CreatorMessageChecker


class MessageManager(ObjManager):
    def __init__(self, message: Message):
        self.message = message
        self.member = self.message.from_user
        self.group = self.message.chat

    async def check(self):
        print('check in MessageManager')
        # TODO: если ты уже понял, как сохранять настройки группы, измени эту мидлварь
        member_manager = MemberManager(self.message)
        member_status = await member_manager.get_status_member()
        violation = []

        try:
            if member_status == 'new_member':
                message_checker = NewMemberMessageChecker(self.message)
                if await message_checker.flood_check():
                    violation.append('flood')
                if await message_checker.url_check():
                    violation.append('url')
                elif await message_checker.ban_words_check():
                    violation.append('ban_words')

            elif member_status == 'middle_member':
                message_checker = MiddleMemberMassageChecker(self.message)
                if await message_checker.flood_check():
                    violation.append('flood')
                if await message_checker.url_check():
                    violation.append('url')
                elif await message_checker.ban_words_check():
                    violation.append('ban_words')

            elif member_status == 'admin':
                message_checker = AdminMessageChecker(self.message)
                if await message_checker.flood_check():
                    violation.append('flood')
                if await message_checker.url_check():
                    violation.append('url')
                elif await message_checker.ban_words_check():
                    violation.append('ban_words')

            else:
                message_checker = CreatorMessageChecker(self.message)
                if await message_checker.flood_check():
                    violation.append('flood')
                if await message_checker.url_check():
                    violation.append('url')
                elif await message_checker.ban_words_check():
                    violation.append('ban_words')

            return member_status, violation

        except(ValueError, TypeError) as e:
            if isinstance(e, TypeError):
                print(f"TypeError: {e}")
                print(f"Current object: {self}")
            else:
                print(f"ValueError: {e}")
                print(f"Current object: {self}")
                raise e
