from aiogram.types import Message


async def on_new_message_from_creator(message: Message):
    await message.chat.unban(195902353)
    # pass