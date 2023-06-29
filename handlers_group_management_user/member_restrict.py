from aiogram.types import Message
import json
import datetime
from constants import RESTRICT_DURATION_MIN
from bot import bot


async def restrict_member(message: Message) -> None:
    permissions = {
                    "can_send_messages": False,
                    "can_send_media_messages": False,
                    "can_send_polls": False,
                    "can_send_other_messages": False,
                    "can_add_web_page_previews": False,
                    "can_change_info": False,
                    "can_invite_users": False,
                    "can_pin_messages": False
                   }

    permissions_json = json.dumps(permissions)
    current_date = datetime.datetime.now()
    next_day = current_date + datetime.timedelta(minutes=RESTRICT_DURATION_MIN)

    print('before restricted')
    await bot.restrict_chat_member(message.chat.id,
                                   message.from_user.id,
                                   permissions=permissions_json,
                                   until_date=next_day)
    print('after restricted')

