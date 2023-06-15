from aiogram import Router
from aiogram.types import Message
import datetime


router = Router()


@router.message()
async def on_chat_member_update(message: Message):
    keys = ['user_id', 'chat_id', 'date_join', 'date_message']

    data_join = message.new_chat_members
    data_join_flag = False
    if data_join is not None:
        data_join_flag = True

    member_data = {'user_id': message.from_user.id,
                   'chat_id': message.chat.id,
                   'data_join': message.new_chat_members,
                   'data_message': message.date
                    }
#
#     mem
#
#     member_data = {key: json_data.get(key) for key in keys}
#     for keys, value in member_data.items():
#         print(keys, value)
    print(data_join_flag)


