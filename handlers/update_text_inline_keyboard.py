from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress
from keyboards.management_group_inline_keyboard import group_management_inline_keyboard
from texts_of_message import text_check_membership


async def update_text_inline_keyboard(message: Message, chat_id: int, pattern):
    with suppress(TelegramBadRequest):
        print('text_inline_keyboard')
        if pattern == 'group_management':
            await message.edit_text(text_check_membership,
                                    reply_markup=group_management_inline_keyboard(chat_id))
