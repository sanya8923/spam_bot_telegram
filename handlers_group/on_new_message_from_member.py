from aiogram.types import Message
from typing import Coroutine

from handlers_group.on_new_message_from_new_member import on_new_message_from_new_member
from handlers_group.on_new_message_from_ordinary_member import on_new_message_from_ordinary_member

from handlers_group_management_message.check_ban_words import check_ban_words

from handlers_group_management_user.member_ban import ban_member
from handlers_group_management_user.check_new_member import check_new_member


async def on_new_message_from_member(message: Message) -> Coroutine:

    presence_ban_word = await check_ban_words(message)
    if presence_ban_word:
        await message.delete()
        await ban_member(message)
    else:
        new_member = await check_new_member(message)
        if new_member:
            return await on_new_message_from_new_member(message)
        else:
            return await on_new_message_from_ordinary_member(message)
