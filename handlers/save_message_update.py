from aiogram import Router
from aiogram.types import Message
import datetime


router = Router()


@router.message()
async def save_message_update(message: Message):
    members_data = []
    member_data = {'user_id': message.from_user.id,
                   'chat_id': message.chat.id,
                   'date_message': message.date
                   }

    data_join = message.new_chat_members
    data_join_flag = False
    if data_join is not None:
        data_join_flag = True

    member_data['join_message'] = data_join_flag

    members_data.append(member_data)

    for line in members_data:
        print(line['data_message'])


# on_chat_member_update