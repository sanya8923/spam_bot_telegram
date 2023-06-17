from aiogram import Router
from aiogram.types import Message
from typing import Optional
import datetime


router = Router()
members_data = []


class MessageUpdate:
    user_id: int
    chat_id: int
    message_id: int
    date_message: int
    join_message: Optional[bool] = False


@router.message()
async def save_message_update(message: Message):
    item = MessageUpdate()
    item.user_id = message.from_user.id
    item.chat_id = message.chat.id
    item.message_id = message.message_id
    item.date_message = message.date

    data_join = message.new_chat_members
    if data_join is not None:
        item.join_message = True

    members_data.append(item)
    for line in members_data:
        print(f'user_id: {line.user_id}'
              f'\nchat_id: {line.chat_id}'
              f'\nmessage_id: {line.message_id}'
              f'\ndate_message: {line.date_message}')

