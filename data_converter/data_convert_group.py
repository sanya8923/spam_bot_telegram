from data_converter import DataConverter
from data.data import UserData, GroupData, MessageData
from typing import Union
from aiogram.types import Message


class DataConverterGroup(DataConverter):
    async def get_data_to_dict(self, obj: GroupData) -> dict:
        print('get_data_to_dict in DataConverterGroup')
        return {'user': 18}


