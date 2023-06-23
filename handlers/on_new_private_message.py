from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def on_new_private_message(message: Message):
    pass
