from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress
from keyboards.inline_keyboards import setting_group_inline_keyboard, management_admins_inline_keyboard, \
    members_management_inline_keyboard, choice_groups_inline_keyboard, group_management_inline_keyboard, \
    button_update_groups_list
from texts_of_message import text_check_membership, text_choice_group, text_not_group, text_members_management, \
    text_admins_management, text_setting_group
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
                                    reply_markup=members_management_inline_keyboard(chat_id, user_id))

        elif pattern == 'admins_management':
            await message.edit_text(text_admins_management,
                                    reply_markup=management_admins_inline_keyboard(chat_id, user_id))

        elif pattern == 'setting_group':
            await message.edit_text(text_setting_group,
                                    reply_markup=setting_group_inline_keyboard(chat_id, user_id))

        else:
            await message.edit_text(text_not_group,
                                    reply_markup=button_update_groups_list(user_id))
