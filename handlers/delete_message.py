from aiogram import Router
from aiogram.types import Message


router = Router()


async def delete_message(chat_id: int, message_id: int):
    await delete_message(chat_id=chat_id, message_id=message_id)

