from aiogram.types import Message


async def unban_members(message: Message):
    if message.text == 'unban':
        await message.chat.unban(195902353)
