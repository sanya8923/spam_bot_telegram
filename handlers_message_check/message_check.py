from aiogram import Router
from aiogram.types import Message

from handlers_message_check.get_status_member import new_member_checkin
from handlers.save_message_update import save_message_update
from handlers_user_management.ban_member import ban_member
from handlers_message_check.checking_for_url import checking_for_url
from handlers_message_check.check_message_frequency import check_message_frequency
from handlers_user_management.restrict_member import restrict_member


router = Router()


@router.message()
async def message_check(message: Message):
    await save_message_update(message)
    new_member = await new_member_checkin(message)
    url_presence = await checking_for_url(message)

    if new_member and url_presence:
        await message.delete()
        await ban_member(bot,
                         message,
                         ban_duration_min=1440)

    posting_too_often = await check_message_frequency(message,
                                                      duration_of_check_min=60,
                                                      number_of_messages=5)

    if posting_too_often:
        await restrict_member(bot,
                              message,
                              restrict_duration_min=10)
