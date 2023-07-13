from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardMarkup


def members_management_inline_keyboard(chat_id: int, user_id: int):
    print('members_management_inline_keyboard')

    buttons = [
        [InlineKeyboardButton(text='Забанить участника', callback_data='ban_user')],
        [InlineKeyboardButton(text='Разбанить участника', callback_data='unban_user')],
        [InlineKeyboardButton(text='Замьютить участника', callback_data='mute_user')],
        [InlineKeyboardButton(text='Размьютить участника', callback_data='unmute_user')],
        [InlineKeyboardButton(text='Назад', callback_data=f'UpdGr_{user_id}')],
        [InlineKeyboardButton(text='К списку групп', callback_data=f'UpdGr_{user_id}')],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)
