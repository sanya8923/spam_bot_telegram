from aiogram import Router
from aiogram.types import Message
from handlers_private.bot_start import cmd_start


router = Router()


@router.message()
async def on_new_message_private(message: Message):
    if message == '/start':
        await cmd_start(message)
