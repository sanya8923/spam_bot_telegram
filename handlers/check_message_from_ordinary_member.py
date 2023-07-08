from aiogram.types import Message
from typing import Coroutine

from handlers.check_message_frequency import check_message_frequency

from handlers.member_restrict import restrict_member


async def check_message_from_ordinary_member(message: Message) -> Coroutine:
    print('on_new_message_from_ordinary_member')
    posting_too_often = await check_message_frequency(message)
    if posting_too_often:
        await restrict_member(message)