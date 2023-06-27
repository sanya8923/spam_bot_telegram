from aiogram.types import Message


async def member_unban(message: Message):
    if message.text == 'unban':
        await message.chat.unban(195902353)
