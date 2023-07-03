from aiogram import Router
from aiogram.types import Message
from handlers_private.bot_start import cmd_start


router = Router()


@router.message()
async def on_new_message_private(message: Message):
    print('on_new_message_private')
    if message.text == '/start':
        await cmd_start(message)