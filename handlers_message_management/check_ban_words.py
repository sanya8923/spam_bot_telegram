from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def check_ban_words(message: Message) -> bool:
    pass
