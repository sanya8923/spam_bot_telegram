from aiogram import Router, F
from aiogram.types import Message, ChatMemberOwner
import datetime
from constants import BAN_DURATION_MIN

router = Router()
banned_members = []


@router.message()
async def ban_member(bot, message: Message) -> None:
    current_date = datetime.datetime.now()
    next_day = current_date + datetime.timedelta(minutes=BAN_DURATION_MIN)

    banned_members.append(message.from_user.id)
    if message.chat.type != 'private' and not isinstance(message.chat.get_member(message.from_user.id),
                                                         ChatMemberOwner):
        await bot.ban_chat_member(message.chat.id,
                                  message.from_user.id,
                                  until_date=next_day,
                                  revoke_messages=False)




