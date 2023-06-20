from aiogram import Router, F
from aiogram.types import Message
import datetime

from filter.find_link_filter import HasLinkFilter
from handlers.save_message_update import members_data
from middlewares.save_message_update2 import SaveMessageUpdateMiddleware

router = Router()
banned_members = []


@router.message()
async def ban_member(bot, message: Message, ban_duration_min: int) -> None:
    current_date = datetime.datetime.now()
    next_day = current_date + datetime.timedelta(minutes=ban_duration_min)

    banned_members.append(message.from_user.id)

    await bot.ban_chat_member(message.chat.id,
                              message.from_user.id,
                              until_date=next_day,
                              revoke_messages=False)



