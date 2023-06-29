from aiogram import Router
from aiogram.types import Message, Update, update

from handlers_private_chat.check_membership_groups import check_membership_groups


router = Router()


@router.message()
async def on_new_private_message(message: Message):
    await check_membership_groups()
