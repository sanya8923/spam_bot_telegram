from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from handlers_private.check_membership_groups import check_membership_groups
from filter.chat_type_filter import ChatTypeFilter


router = Router()
router.message.filter(ChatTypeFilter(chat_type='private'))


@router.message(Command('start'))
async def cmd_start(message: Message):
    print('cmd_start')
    await message.answer('Welcome')
    await check_membership_groups(message)


@router.message(Command('trututu'))
async def cmd_trututu(message: Message):
    print('cmd_trututu')
    await message.answer('cmd_trututu')