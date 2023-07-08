from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Text
from handlers.check_membership_groups import check_membership_groups
from filter.chat_type_filter import ChatTypeFilter
from keyboards.management_group_inline_keyboard import group_management_inline_keyboard
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest

router = Router()
router.message.filter(ChatTypeFilter(chat_type='private'))


@router.message(Command('start'))
async def cmd_start(message: Message):
    print('cmd_start')
    await message.answer('Welcome')
    await check_membership_groups(message)


@router.callback_query(Text(startswith='cid_'))
async def group_management(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        print('group_management')
        chat_id = int(callback.data.split('_')[1])
        await callback.message.answer('Выберите действие:',
                                      reply_markup=group_management_inline_keyboard(chat_id=chat_id))


@router.callback_query(Text(startswith='uid_'))
async def update_membership_groups(callback: CallbackQuery):
    print('update_membership_groups')
    pass