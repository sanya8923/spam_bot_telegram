from aiogram import Router
from aiogram.types import Message
from handlers_private.check_membership_groups import check_membership_groups


router = Router()


async def cmd_start(message: Message):
    print('cmd_start')
    await message.answer('Welcome')
    await check_membership_groups(message)

