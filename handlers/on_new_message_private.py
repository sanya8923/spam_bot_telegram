from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Text
from handlers.check_membership_groups import check_membership_groups
from handlers.update_text_inline_keyboard import update_text_inline_keyboard
from filter.chat_type_filter import ChatTypeFilter
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from texts_of_message import text_choice_group
from keyboards.choice_groups_inline_keyboard import choice_groups_inline_keyboard

router = Router()
router.message.filter(ChatTypeFilter(chat_type='private'))


@router.message(Command('start'))
async def cmd_start(message: Message):
    print('cmd_start')
    await message.answer('Welcome')
    chat_data = await check_membership_groups(message)
    await message.answer(text_choice_group, reply_markup=choice_groups_inline_keyboard(message.from_user.id, chat_data))


@router.callback_query(Text(startswith='cid_'))
async def group_management(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        print('group_management')
        chat_id = int(callback.data.split('_')[1])
        pattern = 'group_management'
        await update_text_inline_keyboard(callback.message, chat_id, pattern)


@router.callback_query(Text(startswith='uid_'))
async def update_membership_groups(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        print('update_membership_groups')
        pattern = 'update_membership_groups'
        await update_text_inline_keyboard(callback.message, pattern)

