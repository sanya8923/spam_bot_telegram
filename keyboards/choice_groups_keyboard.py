from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, Message
from texts_of_message import text_choice_group


async def choice_groups_keyboard(message: Message, chat_names: list):
    builder = ReplyKeyboardBuilder()
    chat_name = 0
    username = 1

    for document in chat_names:
        builder.add(KeyboardButton(text=f'{document[chat_name]} \n({document[username]})'))
    builder.adjust(2)
    await message.answer(text_choice_group,
                         reply_markup=builder.as_markup(resize_keyboard=True))

