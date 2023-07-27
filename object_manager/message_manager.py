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
        member_manager = MemberManager(self.member, self.group)
        member_status = await member_manager.get_status_member()
        try:
            if member_status == 'new_member':
                message_checker = NewMemberMessageChecker(self.message)
                await message_checker.flood_check()
                if await message_checker.url_check():
                    pass
                    #  here code about sanctions user
                elif await message_checker.ban_words_check():
                    pass
                    #  here code about sanctions user
                    return True
                else:
                    return False
            elif member_status == 'middle_member':
                message_checker = MiddleMemberMassageChecker(self.message)
                await message_checker.flood_check()
                if await message_checker.url_check():
                    pass
                    #  here code about sanctions user
                elif await message_checker.ban_words_check():
                    pass
                    #  here code about sanctions user
                    return True
                else:
                    return False
            elif member_status == 'admin':
                message_checker = AdminMessageChecker(self.message)
                if await message_checker.url_check():
                    pass
                    #  here code about sanctions user
                elif await message_checker.ban_words_check():
                    pass
                    #  here code about sanctions user
                    return True
                else:
                    return False
            else:
                message_checker = CreatorMessageChecker(self.message)
                #  here code about sanctions user
                return False

        except (ValueError, TypeError) as e:
            raise (ValueError, TypeError)
