from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message()
async def posting_too_often(message: Message):
    user_id = message.from_user.id
    date_message = message.date
    print(f'user {user_id} send message {date_message}')
    print(message.json(indent=4))
