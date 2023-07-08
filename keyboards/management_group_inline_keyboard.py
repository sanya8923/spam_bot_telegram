from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


def group_management_inline_keyboard(chat_id: int):
    print('group_management_inline_keyboard')
    buttons = [
        [InlineKeyboardButton(text='Управление участниками', callback_data='management_members')],
        [InlineKeyboardButton(text='Управление администраторами', callback_data='management_admins')],
        [InlineKeyboardButton(text='Управление группой', callback_data='management_group')],
        [InlineKeyboardButton(text='Быстрая настройка группы', callback_data='quick_setting_group')],
        [InlineKeyboardButton(text='Обратная связь', callback_data='feedback')],
        [InlineKeyboardButton(text='Назад', callback_data='back')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)

