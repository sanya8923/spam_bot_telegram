from aiogram import Router, F
from aiogram.types import Message
import datetime

from filter.find_link import HasLinkFilter
from handlers.save_message_update import members_data
from middlewares.save_message_update2 import SaveMessageUpdateMiddleware

router = Router()


@router.message()
async def ban_member(message: Message, bot):
    current_date = datetime.datetime.now()
    next_day = current_date + datetime.timedelta(days=1)

    await bot.ban_chat_member(message.chat.id,
                              message.from_user.id,
                              until_date=next_day,
                              revoke_messages=False)




