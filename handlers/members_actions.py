from aiogram.types import Message, ChatMemberOwner
import datetime
import json
from constants import BAN_DURATION_MIN, RESTRICT_DURATION_MIN
from bot import bot
from db.db_mongodb import add_banned_member_to_collection


async def ban_member(message: Message) -> None:
    current_date = datetime.datetime.now()
    next_day = current_date + datetime.timedelta(minutes=BAN_DURATION_MIN)

    if message.chat.type != 'private' and not isinstance(message.chat.get_member(message.from_user.id),
                                                         ChatMemberOwner):
        await add_banned_member_to_collection(message.chat.id, message.from_user.id, message.date)
        await bot.ban_chat_member(message.chat.id,
                                  message.from_user.id,
                                  until_date=next_day,
                                  revoke_messages=False)


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

    await bot.restrict_chat_member(message.chat.id,
                                   message.from_user.id,
                                   permissions=permissions_json,
                                   until_date=next_day)


async def member_unban(message: Message):
    if message.text == 'unban':
        await message.chat.unban(195902353)