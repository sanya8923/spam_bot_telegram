from aiogram import Router
from aiogram.types import Message
from typing import Coroutine

from handlers_message_management.check_message_for_url import check_for_url
from handlers_message_management.check_message_frequency import check_message_frequency

from handlers_user_management.member_ban import ban_member
from handlers_user_management.member_restrict import restrict_member

from handlers_message_management.save_message_update import save_message_update


router = Router()


@router.message()
async def on_new_message_from_new_member(message: Message) -> Coroutine:
    presence_url = await check_for_url(message)
    if presence_url:
        await message.delete()
        await ban_member(message)
    else:
        posting_too_often = await check_message_frequency(message)
        if posting_too_often:
            await restrict_member(message)
        else:
            return await save_message_update(message)
