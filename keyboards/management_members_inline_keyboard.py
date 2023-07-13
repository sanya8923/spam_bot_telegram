from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardMarkup


def members_management_inline_keyboard(chat_id: int, user_id: int):
    print('members_management_inline_keyboard')

    buttons = [
        [InlineKeyboardButton(text='Забанить участника', callback_data=f'ban_user_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Разбанить участника', callback_data=f'unban_user_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Замьютить участника', callback_data=f'mute_user_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Размьютить участника', callback_data=f'unmute_user_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='Назад', callback_data=f'GrMan_{user_id}_{chat_id}')],
        [InlineKeyboardButton(text='К списку групп', callback_data=f'UpdGr_{user_id}')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)
