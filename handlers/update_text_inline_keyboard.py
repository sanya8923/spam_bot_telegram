from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress
from keyboards.management_group_inline_keyboard import group_management_inline_keyboard
from keyboards.choice_groups_inline_keyboard import choice_groups_inline_keyboard
from keyboards.button_update_groups_list import button_update_groups_list
from keyboards.management_members_inline_keyboard import members_management_inline_keyboard
from texts_of_message import text_check_membership, text_choice_group, text_not_group, text_members_management
from handlers.check_membership_groups import check_membership_groups


async def update_text_inline_keyboard(**kwargs):
    pattern = kwargs.get('pattern')
    message = kwargs.get('message')
    chat_id = kwargs.get('chat_id')
    user_id = kwargs.get('user_id')

    with suppress(TelegramBadRequest):
        if pattern == 'group_management':
            await message.edit_text(text_choice_group,
                                    reply_markup=group_management_inline_keyboard(chat_id, user_id))

        elif pattern == 'update_membership_groups':
            chat_data = await check_membership_groups(user_id)

            if len(chat_data) > 0:
                await message.edit_text(text_check_membership,
                                        reply_markup=choice_groups_inline_keyboard(user_id, chat_data))

        elif pattern == 'members_management':
            await message.edit_text(text_members_management,
                                    reply_markup=members_management_inline_keyboard(user_id))

        else:
            await message.edit_text(text_not_group,
                                    reply_markup=button_update_groups_list(user_id))
