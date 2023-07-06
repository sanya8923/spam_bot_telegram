from aiogram.types import Message

from handlers_group_management_message.check_message_for_url import check_for_url
from handlers_group_management_message.check_message_frequency import check_message_frequency

from handlers_group_management_user.member_ban import ban_member
from handlers_group_management_user.member_restrict import restrict_member


async def on_new_message_from_new_member(message: Message):
    presence_url = await check_for_url(message)
    if presence_url:
        await message.delete()
        await ban_member(message)
    else:
        posting_too_often = await check_message_frequency(message)
        if posting_too_often:
            await restrict_member(message)
