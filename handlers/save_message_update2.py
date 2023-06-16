from aiogram import Router
from aiogram.types import Message
from aiogram.filters import BaseFilter
from typing import Dict, List, Optional
import datetime


router = Router()
members_data = []


@router.message()
async def save_mes_up(message: Message) -> List[Dict]:
    member_data = {'user_id': message.from_user.id,
                   'chat_id': message.chat.id,
                   'message_id': message.message_id,
                   'date_message': message.date,
                   'join_message': False}

    data_join = message.new_chat_members
    if data_join is not None:
        member_data['join_message'] = True

    members_data.append(member_data)

    print(f'members_data: {members_data}')

