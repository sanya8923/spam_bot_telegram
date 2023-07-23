from data_converter import DataConverter
from data.data import UserData, GroupData, MessageData
from typing import Union


class DataConverterUsers(DataConverter):
    async def get_data_to_dict(self, obj: Union[UserData, GroupData, MessageData]) -> dict:
        print('get_data_to_dict in DataConverterUsers')
        return {'user': 18}
