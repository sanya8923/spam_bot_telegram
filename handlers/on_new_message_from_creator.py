from aiogram.types import Message


async def on_new_message_from_creator(message: Message):
    await message.chat.unban(5430126145)
    # pass