from data.data import UserData, GroupData, MessageData
from typing import Union
from aiogram.types import Message
from db_manager.db_manager import DbManager
from data_converter.data_convert_group import DataConverterGroup
from data_converter.data_converter_message import DataConverterMessage
from data_converter.data_converter_users import DataConverterUsers
from data_converter.data_converter import DataConverter


class DataManager:
    def __init__(self):
        # self.object =
        pass

    async def save_message(self, message: Message) -> MessageData:
        print('save_objects')

        await DataConverterMessage().save_message(message)



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
