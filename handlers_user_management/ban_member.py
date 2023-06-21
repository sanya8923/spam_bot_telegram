from aiogram import Router, F
from aiogram.types import Message, ChatMemberOwner
import datetime

router = Router()
banned_members = []


@router.message()
async def ban_member(bot, message: Message, ban_duration_min: int) -> None:
    current_date = datetime.datetime.now()
    next_day = current_date + datetime.timedelta(minutes=ban_duration_min)

    banned_members.append(message.from_user.id)
    if message.chat.type != 'private' and not isinstance(message.chat.get_member(message.from_user.id),
                                                         ChatMemberOwner):
        await bot.ban_chat_member(message.chat.id,
                                  message.from_user.id,
                                  until_date=next_day,
                                  revoke_messages=False)




