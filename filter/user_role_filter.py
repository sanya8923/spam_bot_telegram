from typing import Union
from aiogram.filters import BaseFilter
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.types import Message
from bot import bot


class UserRoleFilter(BaseFilter):
    def __init__(self, user_role):
        self.user_role = user_role

    async def __call__(self, message: Message):
        get_chat_member = GetChatMember(
            chat_id=message.chat.id,
            user_id=message.from_user.id
        )
        chat_status = await bot.__call__(get_chat_member)

        if isinstance(self.user_role, str):
            return chat_status.status == self.user_role
        else:
            return chat_status.status in self.user_role

