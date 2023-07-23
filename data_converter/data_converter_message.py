from data_converter import DataConverter
from data.data import UserData, GroupData, MessageData
from typing import Union


class DataConverterMessage(DataConverter):
    async def get_data_to_dict(self, obj: MessageData) -> dict:
        print('get_data_to_dict in DataConverterMessage')
        return {'user': 18}
