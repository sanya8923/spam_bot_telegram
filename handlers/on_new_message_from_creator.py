from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def on_new_message_from_creator(message: Message):
    pass
