from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardMarkup


def setting_group_inline_keyboard(chat_id: int, user_id: int):
    print('setting_group_inline_keyboard')

    buttons = [
        [InlineKeyboardButton(text='Управление бан-словами', callback_data='BanWords_')]
    ]

