from aiogram import Router
from aiogram.types import Message
from typing import Coroutine

from handlers_message_management.check_message_frequency import check_message_frequency

from handlers_user_management.member_restrict import restrict_member

from handlers_message_management.save_message_update import save_message_update

from bot import bot


router = Router()


@router.message()
async def on_new_message_from_ordinary_member(message: Message) -> Coroutine:
    print('on_new_message_from_ordinary_member')
    posting_too_often = await check_message_frequency(message)
    if posting_too_often:
        await restrict_member(message)
    else:
        return await save_message_update(message)
