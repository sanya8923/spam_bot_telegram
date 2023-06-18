from aiogram import Router
from aiogram.types import Message
from handlers.save_message_update import members_data


router = Router()


@router.message()
async def check_message_frequency(message: Message):
    pass

