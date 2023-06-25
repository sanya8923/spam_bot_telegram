from aiogram import Router
from aiogram.types import Message
from aiogram.methods.get_chat_member import GetChatMember
from typing import Coroutine
from bot import bot


router = Router()


@router.message()
async def get_member_status_group_supergroup(message: Message) -> Coroutine:

    get_chat_member = GetChatMember(
        chat_id=message.chat.id,
        user_id=message.from_user.id
    )
    chat_status = await bot.__call__(get_chat_member)
    return chat_status.status
