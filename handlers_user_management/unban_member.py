from aiogram import Router
from aiogram.types import Message

from bot import bot


router = Router()


@router.message()
async def unban_members(message: Message):
    if message.text == 'unban':
        await message.chat.unban(195902353)
