from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def check_message_frequency(message: Message):
    pass

