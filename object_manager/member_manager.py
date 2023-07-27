from object_manager.object_manager import ObjManager
from bot import bot
from aiogram.types import TelegramObject


class MemberManager(ObjManager):
    def __init__(self, member: TelegramObject, group: TelegramObject):
        self.member = member
        self.group = group

    async def check(self):
        print('check in MemberManager')
        pass

    async def get_status_member(self) -> str:
        print('get_status_member in MemberManager')
        member = await bot.get_chat_member(self.group.id, self.member.id)
        return member.status
