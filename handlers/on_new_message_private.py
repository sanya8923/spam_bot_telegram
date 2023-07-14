from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Text
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

from contextlib import suppress

from db.db_mongodb import get_membership_groups, add_banned_member_to_collection, get_user_role

from handlers.update_text_inline_keyboard import update_text_inline_keyboard

from filter.chat_type_filter import ChatTypeFilter
from filter.state import MyState

from texts_of_message import text_choice_group, text_not_group, text_ban_user_from_private
from keyboards.inline_keyboards import choice_groups_inline_keyboard, button_update_groups_list


router = Router()
router.message.filter(ChatTypeFilter(chat_type='private'))


@router.message(Command('start'))
async def cmd_start(message: Message):
    with suppress(TelegramBadRequest):
        print('cmd_start')
        await message.answer('Welcome')

        user_id = message.from_user.id
        chat_data = await get_membership_groups(user_id)

        if len(chat_data) > 0:
            await message.answer(text_choice_group,
                                 reply_markup=choice_groups_inline_keyboard(
                                     user_id=user_id,
                                     chat_data=chat_data))
        else:
            await message.answer(text_not_group,
                                 reply_markup=button_update_groups_list(message.from_user.id))


@router.callback_query(Text(startswith='GrMan_'))
async def group_management(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        print('group_management')
        callback_data = callback.data.split('_')
        user_id = int(callback_data[1])
        chat_id = int(callback_data[2])
        pattern = 'group_management'
        await update_text_inline_keyboard(message=callback.message,
                                          chat_id=chat_id,
                                          user_id=user_id,
                                          pattern=pattern)


@router.callback_query(Text(startswith='UpdGr_'))
async def update_membership_groups(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        print('update_membership_groups')
        user_id = int(callback.data.split('_')[1])

        pattern = 'update_membership_groups'
        await update_text_inline_keyboard(message=callback.message,
                                          user_id=user_id,
                                          pattern=pattern)


@router.callback_query(Text(startswith='MembManag_'))
async def members_management(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        print('members_management')
        callback_data = callback.data.split('_')
        user_id = int(callback_data[1])
        chat_id = int(callback_data[2])

        pattern = 'members_management'
        await update_text_inline_keyboard(message=callback.message,
                                          user_id=user_id,
                                          chat_id=chat_id,
                                          pattern=pattern)


@router.callback_query(Text(startswith='Amanagement_'))
async def admins_management(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        print('admins_management')
        callback_data = callback.data.split('_')
        user_id = int(callback_data[1])
        chat_id = int(callback_data[2])

        pattern = 'admins_management'
        await update_text_inline_keyboard(message=callback.message,
                                          user_id=user_id,
                                          chat_id=chat_id,
                                          pattern=pattern)


@router.callback_query(Text(startswith='setting_'))
async def setting_group(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        print('setting_group')
        callback_data = callback.data.split('_')
        user_id = int(callback_data[1])
        chat_id = int(callback_data[2])

        pattern = 'setting_group'
        await update_text_inline_keyboard(message=callback.message,
                                          user_id=user_id,
                                          chat_id=chat_id,
                                          pattern=pattern)


@router.callback_query(Text(startswith='BanUser_'))
async def ban_member_from_private(callback: CallbackQuery, state: FSMContext):
    print('ban_member_private')

    await callback.message.answer(text_ban_user_from_private)
    await state.set_state(MyState.waiting_message_for_ban_user)





