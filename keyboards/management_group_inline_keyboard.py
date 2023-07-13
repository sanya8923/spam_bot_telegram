from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


def group_management_inline_keyboard(chat_id: int, user_id: int):
    print('group_management_inline_keyboard')
    buttons = [
        [InlineKeyboardButton(text='Управление участниками', callback_data=f'MembManag_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Управление администраторами', callback_data=f'Amanagement_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Управление группой', callback_data=f'setting_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Быстрая настройка группы', callback_data=f'Qsetting_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Обратная связь', callback_data=f'feedback_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Назад', callback_data=f'UpdGr_{user_id}')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)

