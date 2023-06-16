from aiogram import Router
from aiogram.types import Message
from aiogram.filters import BaseFilter
from typing import Dict, List, Optional
import datetime


router = Router()
members_data = []


class MessageUpdate:
    user_id: int
    chat_id: int
    message_id: int
    date_message: datetime
    join_message: Optional[bool] = False

    @router.message()
    async def save_mes_up(self, message: Message):
        item = MessageUpdate
        item.user_id = message.from_user.id
        item.chat_id = message.chat.id
        item.message_id = message.message_id
        item.date_message = message.date

        data_join = message.new_chat_members
        if data_join is not None:
            item.join_message = True

        members_data.append(item)

