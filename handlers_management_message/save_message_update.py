from aiogram.types import Message
from typing import Optional

from db.db_mongodb import add_message_update_to_collection
from handlers_management_user.member_unban import member_unban


class MessageUpdate:
    user_id: int
    chat_id: int
    message_id: int
    date_message: int
    join_message: Optional[bool] = False


async def save_message_update(message: Message):
    item = MessageUpdate()
    item.user_id = message.from_user.id
    item.chat_id = message.chat.id
    item.message_id = message.message_id
    item.date_message = message.date

    data_join = message.new_chat_members
    if data_join is not None:
        item.join_message = True

    await add_message_update_to_collection(item)

