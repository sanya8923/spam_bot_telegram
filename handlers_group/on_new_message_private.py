from aiogram import Router
from aiogram.types import Message, Update, update

from handlers_private.check_membership_groups import check_membership_groups


router = Router()


@router.message()
async def on_new_message_private(message: Message):
    await check_membership_groups()
