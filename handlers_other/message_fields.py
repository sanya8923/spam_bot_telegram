from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def posting_too_often(message: Message):
    print(message.json(indent=4))
