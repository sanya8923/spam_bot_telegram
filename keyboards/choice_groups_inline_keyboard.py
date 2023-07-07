from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import Message, InlineKeyboardButton
from texts_of_message import text_choice_group


user_data = {}


def choice_groups_inline_keyboard(message: Message, chat_names: list):
    print('choice_group_inline_keyboard')

    chat_name = 0
    username = 1
    chat_id = 2

    buttons = [[InlineKeyboardButton(text=f'{item[chat_name]} (@{item[username]})', callback_data=f'cid_{item[chat_id]}')]
               for item in chat_names]
    buttons.append([InlineKeyboardButton(text='Обновить список чатов', callback_data=f'uid_{message.from_user.id}')])

    return InlineKeyboardMarkup(inline_keyboard=buttons)


async def choice_groups(message: Message, chat_names: list):
    print('choice_groups')
    await message.answer('Выберите группу:', reply_markup=choice_groups_inline_keyboard(message, chat_names))

