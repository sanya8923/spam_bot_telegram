from data.data import UserData, GroupData, MessageData
from typing import Union
from aiogram.types import Message
from db_manager.db_manager import DbManager
from data_converter.data_convert_group import DataConverterGroup
from data_converter.data_converter_message import DataConverterMessage
from data_converter.data_converter_users import DataConverterUsers


class DataManager:
    def __init__(self):
        # self.object =
        pass

    async def save_message(self, message: Message) -> MessageData:
        print('save_objects')

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
        message_data.entities_type = message.entities['type']
        message_data.from_user = from_user
        message_data.from_chat = from_chat

        return message_data

    async def get_data_to_dict(self, obj: Union[list, UserData, GroupData, MessageData]):
        print('get_data_to_dict')

        if isinstance(obj, UserData):
            return await DataConverterUsers().get_data_to_dict(obj)
        elif isinstance(obj, GroupData):
            return await DataConverterGroup().get_data_to_dict(obj)
        elif isinstance(obj, MessageData):
            return await DataConverterMessage().get_data_to_dict(obj)
        else:
            raise TypeError

    async def save_to_db(self, data: Union[list, UserData, GroupData, MessageData]):
        print('save_to_db')
        await DataManager().save_to_db(data)
        print('save_to_db')
