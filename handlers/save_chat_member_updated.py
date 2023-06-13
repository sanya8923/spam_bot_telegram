from aiogram.types import Message, ChatMemberUpdated
from aiogram import Router


router = Router()


async def save_chat_member_updated(message: Message):
    member_updated = {}
    new_chat_member = message.new_chat_members

