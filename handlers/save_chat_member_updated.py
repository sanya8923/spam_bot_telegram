from aiogram import Router
from aiogram.types import Message
import datetime


router = Router()


@router.message()
async def on_chat_member_update(message: Message):
    member_data = {'user_id': message.from_user.id,
                   'chat_id': message.chat.id,
                   'data_message': message.date
                   }

    data_join = message.new_chat_members
    data_join_flag = False
    if data_join is not None:
        data_join_flag = True

    member_data['join_message'] = data_join_flag

    for keys, value in member_data.items():
        print(keys, value)


