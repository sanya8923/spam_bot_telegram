from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardMarkup


def management_members_inline_keyboard(chat_id: int):
    print('management_members_inline_keyboard')

    buttons = [
        [InlineKeyboardButton(text='Забанить участника', callback_data='ban_user')]
        [InlineKeyboardButton(text='Разбанить участника', callback_data='unban_user')]
        [InlineKeyboardButton(text='Замьютить участника', callback_data='mute_user')]
        [InlineKeyboardButton(text='Размьютить участника', callback_data='unmute_user')]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)
