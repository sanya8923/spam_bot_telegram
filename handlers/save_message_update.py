from aiogram import Router
from aiogram.types import Message
from aiogram.filters import BaseFilter
from typing import Dict, List, Optional
import datetime


router = Router()


class MessageUpdate(BaseFilter):
    user_id: int
    chat_id: int
    message_id: int
    date_message: datetime
    join_message: Optional[bool]

    async def __call__(self, message: Message) -> List[Dict]:
        members_data = []
        item = MessageUpdate
        item.user_id = message.from_user.id
        item.chat_id = message.chat.id
        item.message_id = message.message_id
        item.date_message = message.date

        data_join = message.new_chat_members
        data_join_flag = False
        if data_join is not None:
            data_join_flag = True

        item.join_message = data_join_flag

        members_data.append(item)

        for line in members_data:
            print(line)

        return members_data





# on_chat_member_update