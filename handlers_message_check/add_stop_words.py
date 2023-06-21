from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandObject, Command


router = Router()
# router.message.filter(chat.type == 'private')

stop_words = []


@router.message(Command('add_stop_words'))
async def add_stop_words(message: Message, command: CommandObject):
    if command.args:
        stop_words.extend(command.args.split())
        await message.answer(f'Words {stop_words} added')
