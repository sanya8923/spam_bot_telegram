from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


def choice_groups_inline_keyboard(user_id, chat_names: list):
    print('choice_group_inline_keyboard')
    chat_name = 0
    username = 1
    chat_id = 2

    buttons = [
        [InlineKeyboardButton(text=f'{item[chat_name]} (@{item[username]})', callback_data=f'cid_{item[chat_id]}')]
        for item in chat_names
    ]
    buttons.append([InlineKeyboardButton(text='Обновить список чатов', callback_data=f'uid_{user_id}')])

    return InlineKeyboardMarkup(inline_keyboard=buttons)



