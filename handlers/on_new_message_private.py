from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Text
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext

from contextlib import suppress

from db.db_mongodb import get_membership_groups, get_user_data_from_users, get_users_by_role, \
    update_role_to_db, get_user_role_from_db

from handlers.update_text_inline_keyboard import update_text_inline_keyboard
from handlers.members_actions import restrict_admin_to_member, unban_member

from filter.chat_type_filter import ChatTypeFilter
from filter.state import MyState

from texts_of_message import text_choice_group, text_not_group, text_ban_user_from_private, \
    text_user_banned_from_private, text_admin_try_ban_admin, text_user_already_kicked, text_user_left, \
    text_banned_user_is_creator, text_user_not_found, text_unban_user_true, text_unban_user_false, \
    text_user_unbanned_from_private, text_unban_user_not_found, text_incorrect_username_for_unban, \
    text_mute_user_from_private, text_choice_term_mute_user, text_admin_try_mute_admin, text_muted_user_is_creator
from keyboards.inline_keyboards import choice_groups_inline_keyboard, button_update_groups_list, \
    members_management_inline_keyboard, button_return_to_member_management, term_mute_inline_keyboard

from bot import bot

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
    user_id = int(callback.data.split('_')[1])
    chat_id = int(callback.data.split('_')[2])
    message_id = callback.message.message_id
    chat_private_id = callback.message.chat.id

    await state.update_data(user_id=user_id,
                            chat_id=chat_id,
                            message_id=message_id,
                            chat_private_id=chat_private_id)

    await callback.message.edit_text(text_ban_user_from_private,
                                     reply_markup=button_return_to_member_management(chat_id, user_id))
    await state.set_state(MyState.waiting_message_for_ban_user)


@router.message(MyState.waiting_message_for_ban_user)
async def ban_member_from_private_message(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id_who_ban = data.get('user_id')
    chat_id = data.get('chat_id')
    message_id = data.get('message_id')
    chat_private_id = data.get('chat_private_id')

    entities = message.entities or []

    with suppress(TelegramBadRequest):
        if len(entities) > 0:
            found_username = [item.extract_from(message.text) for item in entities if item.type == 'mention'][0]
            username = found_username[1:]
            user_id_for_ban = int((await get_data_from_db('username', username, 'users'))['user_id'])
        else:
            username = message.text

            user_data = await get_data_from_db('username', username, 'users')
            user_id_for_ban = int(user_data['user_id']) if user_data is not None else None

        if user_id_for_ban is not None:
            print('role_user_who_ban - not None')
            banned_user_data = await bot.get_chat_member(chat_id, user_id_for_ban)
            banned_user_role = banned_user_data.status

                if role_banned_user_from_get_member == 'member':
                    await bot.ban_chat_member(chat_id, user_id_for_ban)
                    await state.clear()
                    await message.answer(text_user_banned_from_private,
                                         reply_markup=members_management_inline_keyboard(chat_id, user_id_who_ban))
                    await bot.delete_message(chat_private_id, message_id)


            else:
                print('Ты что-то не предусмотрел')  # TODO: поменяй
        else:
            await message.answer(text_ban_user_not_found,
                                 reply_markup=button_abolition_ban(chat_id, user_id_who_ban))  # TODO: add button 'ОТМЕНА'


@router.callback_query(Text(startswith='UnbanUser_'))
async def banned_users_list(callback: CallbackQuery, state: FSMContext):
    print('unban_member')
    user_id = int(callback.data.split('_')[1])
    chat_id = int(callback.data.split('_')[2])
    message_id = callback.message.message_id
    chat_private_id = callback.message.chat.id
    banned_users_id = []

    banned_users = (await get_users_by_role(chat_id, 'kicked'))
    print(f'banned_users: {banned_users}')
    if len(banned_users) > 0:
        for user in banned_users:
            banned_users_id.append(user["user_id"])

        banned_users = await get_data_from_db('user_id', banned_users_id, 'users')
        message_banned_users = text_unban_user_true

        count = 1

        for user in banned_users:
            message_banned_users += f'''{count}) Имя: {user["first_name"]} {user["last_name"]}\n
            USERNAME: <code>@{user["username"]}</code>\n\n'''
            count += 1

        await state.update_data(user_id=user_id,
                                chat_id=chat_id,
                                message_id=message_id,
                                chat_private_id=chat_private_id)

        await state.set_state(MyState.waiting_message_for_unban_user)

        await callback.message.edit_text(message_banned_users,
                                         reply_markup=button_return_to_member_management(chat_id, user_id))

    else:
        await callback.message.edit_text(text_unban_user_false,
                                         reply_markup=button_return_to_member_management(chat_id, user_id))


@router.message(MyState.waiting_message_for_unban_user)
async def unban_member_from_private_message(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id_who_unban = data.get('user_id')
    chat_id = data.get('chat_id')
    message_id = data.get('message_id')
    chat_private_id = data.get('chat_private_id')

    entities = message.entities or []

    with suppress(TelegramBadRequest):
        if message.text[0] != '/':
            if len(entities) > 0:
                found_username = [item.extract_from(message.text) for item in entities if item.type == 'mention'][0]
                username = found_username[1:]
                user_id_for_unban = int((await get_data_from_db('username', username, 'users'))['user_id'])
            else:
                username = message.text

                user_data = await get_data_from_db('username', username, 'users')
                user_id_for_unban = int(user_data['user_id']) if user_data is not None else None

            if user_id_for_unban is not None:
                await unban_member(chat_id, user_id_for_unban)
                await update_role_to_db(chat_id, user_id=user_id_for_unban)
                await state.clear()
                await message.answer(text_user_unbanned_from_private,
                                     reply_markup=members_management_inline_keyboard(chat_id,
                                                                                     user_id_who_unban))
            else:
                await message.answer(text_unban_user_not_found,
                                     reply_markup=button_return_to_member_management(chat_id, user_id_who_unban))
        else:
            await message.answer(text_incorrect_username_for_unban,
                                 reply_markup=button_return_to_member_management(chat_id, user_id_who_unban))
        await bot.delete_message(chat_private_id, message_id)


