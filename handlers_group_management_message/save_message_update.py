from aiogram.types import Message
from typing import Optional

from db.db_mongodb import add_data_to_db


class MessageUpdate:
    user_id: int
    chat_id: int
    message_id: int
    date_message: int
    join_message: Optional[bool] = False


async def save_message_update(message: Message):
    data = {
        'date_message': message.date,
        'message_id': message.message_id,
        'user_id': message.from_user.id,
        'chat_id': message.chat.id
    }

    data_join = message.new_chat_members
    if data_join is not None:
        data['join_message'] = True

    collection_name = f'{message.chat.id} - message updates'
    print('in save_message_update')
    await add_data_to_db(collection_name, data)

