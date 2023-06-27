from aiogram.types import Message, ChatMemberOwner
import datetime
from constants import BAN_DURATION_MIN
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




