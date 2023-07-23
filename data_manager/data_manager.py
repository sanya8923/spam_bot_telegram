from data.data import UserData, GroupData, MessageData
from typing import Union
from aiogram.types import Message
from db_manager.db_manager import DbManager
from data_converter.data_convert_group import DataConverterGroup
from data_converter.data_converter_message import DataConverterMessage
from data_converter.data_converter_users import DataConverterUsers
from data_converter.data_converter import DataConverter
from db_manager.db_saver_users import DbSaverUsers
from db_manager.db_saver_groups import DbSaverGroups
from db_manager.db_saver_role import DbSaverRole


class DataManager:
    def __init__(self):
        # self.object =
        pass

    async def save_message(self, message: Message) -> MessageData:
        print('save_objects')
        return await DataConverter().save_message(message)

    async def get_data_to_dict(self, obj: Union[list, UserData, GroupData, MessageData]):
        print('get_data_to_dict')

        if isinstance(obj, UserData):
            return await DataConverterUsers().get_data_to_dict(obj)
        elif isinstance(obj, GroupData):
            return await DataConverterGroup().get_data_to_dict(obj)
        elif isinstance(obj, MessageData):
            return await DataConverterMessage().get_data_to_dict(obj)
        else:
            raise (TypeError, AttributeError, IndexError, ValueError)

    async def save_to_db(self, data: Union[list, UserData, GroupData, MessageData]):
        print('save_to_db in DataManager')
        try:
            data_dict = await DataConverter().get_data_to_dict(data)

            check_user_to_db = await DbSaverUsers().save_to_db(data_dict)
            check_group_to_db = await DbSaverGroups().save_to_db(data_dict)
            check_role_to_db = await DbSaverRole().save_to_db(data_dict)

        except (AttributeError, TypeError, ValueError) as e:
            raise print(f'MyError: {e}')

        if check_user_to_db and check_group_to_db and check_role_to_db is True:
            return True
        else:
            return False

    async def check_message(self, data: MessageData):
        print('check_message in DataManager')


