from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardMarkup


def management_admins_inline_keyboard(chat_id: int, user_id: int):
    print('management_admins_inline_keyboard')

    buttons = [
        [InlineKeyboardButton(text='Назначить администратора', callback_data=f'PromoteAdmin__{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Список администраторов', callback_data=f'AdminsList__{user_id}_{chat_id}')]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)
