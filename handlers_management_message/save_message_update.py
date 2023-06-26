from aiogram import Router
from aiogram.types import Message
from typing import Optional
import datetime

from lists import members_data
from db.db_mongodb import add_message_update_to_collection


router = Router()


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
    print('save_message_update: working')
    if data_join is not None:
        item.join_message = True

    members_data.append(item)
    print('before db')
    await add_message_update_to_collection(item)
    print('after db')
    # chat_id = str(message.chat.id)
    # data = get_data(chat_id[message.message_id])
    # print(data)
    # print(message.json(indent=4))
