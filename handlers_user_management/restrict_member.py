from aiogram import Router, F
from aiogram.types import Message
import json
import datetime


router = Router()


@router.message()
async def restrict_member(bot, message: Message, restrict_duration_min: int) -> None:
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
    next_day = current_date + datetime.timedelta(minutes=restrict_duration_min)

    await bot.restrict_chat_member(message.chat.id,
                                   message.from_user.id,
                                   permissions=permissions_json,
                                   until_date=next_day)
