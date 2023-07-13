from bot import bot
from aiogram.types import Message
from db.db_mongodb import db


async def get_user_role(message: Message):
    print('get_user_role')
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    return user.status
