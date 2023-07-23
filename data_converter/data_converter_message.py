from data_converter import DataConverter
from data.data import UserData, GroupData, MessageData
from typing import Union
from aiogram.types import Message


class DataConverterMessage(DataConverter):
    async def get_data_to_dict(self, obj: MessageData) -> dict:
        print('get_data_to_dict in DataConverterMessage')
        return {'user': 18}

    async def save_message(self, message: Message):
        print('save_message')

        from_user = UserData()
        from_user.id = message.from_user.id
        from_user.username = message.from_user.username
        from_user.first_name = message.from_user.first_name
        from_user.last_name = message.from_user.last_name

        from_chat = GroupData()
        from_chat.id = message.chat.id
        from_chat.type = message.chat.type
        from_chat.chat_username = message.chat.username
        from_chat.chat_name = message.chat.title

        message_data = MessageData()
        message_data.id = message.message_id
        message_data.text = message.text
        message_data.entities_data = message.entities
        message_data.entities_type = message.entities[0]  # TODO: check index
        message_data.from_user = from_user
        message_data.from_chat = from_chat

        return message_data
