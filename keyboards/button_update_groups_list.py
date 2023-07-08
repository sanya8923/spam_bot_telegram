from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardMarkup


def button_update_groups_list(user_id):
    print('button_update_groups_list')
    button = [
        [InlineKeyboardButton(text='Обновить список групп', callback_data=f'uid_{user_id}')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=button)
