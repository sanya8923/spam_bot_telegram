from aiogram import Router
from aiogram.types import Message
from typing import Coroutine

from handlers.on_new_message_from_new_member import on_new_message_from_new_member
from handlers.on_new_message_from_ordinary_member import on_new_message_from_ordinary_member

from handlers_message_management.check_ban_words import check_ban_words

from handlers_user_management.ban_member import ban_member
from handlers_user_management.new_member_checkin import new_member_checkin


router = Router()


@router.message()
async def on_new_message_from_member(message: Message) -> Coroutine:

    presence_ban_word = await check_ban_words(message)
    if presence_ban_word:
        await message.delete()
        await ban_member(message)
    else:
        new_member = await new_member_checkin(message)
        if new_member:
            return await on_new_message_from_new_member(message)
        else:
            return await on_new_message_from_ordinary_member(message)
