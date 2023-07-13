from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardMarkup


def setting_group_inline_keyboard(chat_id: int, user_id: int):
    print('setting_group_inline_keyboard')

    buttons = [
        [InlineKeyboardButton(text='Управление бан-словами', callback_data=f'BanWords_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Срок статуса "новый участник"', callback_data=f'NewMembTerm_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Разрешить ссылки для новых участников', callback_data=f'NewMembLink_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Разрешить ссылки', callback_data=f'Link_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Разрешить пересылку сообщений из др. групп', callback_data=f'Forwarding_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Слишком частый постинг', callback_data=f'TooOftenPost_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Назад', callback_data=f'GrMan_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='К списку групп', callback_data=f'UpdGr_{user_id}')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)

