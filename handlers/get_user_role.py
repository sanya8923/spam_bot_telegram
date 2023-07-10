from bot import bot
from aiogram.types import Message


async def get_user_role(message: Message):
    return bot.get_chat_member(message.chat.id, message.from_user.id)
