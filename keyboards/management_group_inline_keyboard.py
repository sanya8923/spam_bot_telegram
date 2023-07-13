from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


def group_management_inline_keyboard(chat_id: int, user_id: int):
    print('group_management_inline_keyboard')
    buttons = [
        [InlineKeyboardButton(text='Управление участниками', callback_data=f'MembManag_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Управление администраторами', callback_data='Amanagement')],
        [InlineKeyboardButton(text='Управление группой', callback_data='setting')],
        [InlineKeyboardButton(text='Быстрая настройка группы', callback_data='Qsetting')],
        [InlineKeyboardButton(text='Обратная связь', callback_data='feedback')],
        [InlineKeyboardButton(text='Назад', callback_data=f'UpdGr_{user_id}')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)

