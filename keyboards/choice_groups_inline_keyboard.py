from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.types import Message, InlineKeyboardButton
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest

user_data = {}


def choice_groups_inline_keyboard(message: Message, chat_names: list):
    print('choice_group_inline_keyboard')
    chat_name = 0
    username = 1
    chat_id = 2

    buttons = [
        [InlineKeyboardButton(text=f'{item[chat_name]} (@{item[username]})', callback_data=f'cid_{item[chat_id]}')]
        for item in chat_names
    ]
    buttons.append([InlineKeyboardButton(text='Обновить список чатов', callback_data=f'uid_{message.from_user.id}')])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


async def choice_groups(message: Message, chat_names: list):
    with suppress(TelegramBadRequest):
        print('choice_groups')
        await message.answer('Выберите группу:', reply_markup=choice_groups_inline_keyboard(message, chat_names))
