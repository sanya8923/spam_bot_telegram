from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def on_chat_member_update(message: Message):
    keys = ['user_id', 'chat_id', 'date_join', 'date_message']

    if message.new_chat_members is not None:
        data_join = message.date

    # member_data = {user_id: message.from_user.id,
    #                chat_id: message.chat.id,
    #                data_join: lambda (mess)
    #                data_message: message.date
    #                 }
#
#     mem
#
#     member_data = {key: json_data.get(key) for key in keys}
#     print(member_data)


