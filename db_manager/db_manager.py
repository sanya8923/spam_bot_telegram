from db.db_mongodb import Db
from data_manager.data_manager import DataManager
from data.data import UserData, GroupData, MessageData
from typing import Union


class DbManager(Db):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.data: Union[UserData, GroupData, MessageData] = args[0]
        self.data_type: Union[UserData, GroupData, MessageData] = self.data.type
        self._db = Db()
        self._data_manager = DataManager()
        self.dict: dict = await self._data_manager.set_data_to_dict(self.data)
        self._db_result: list = await self._db.get_data()

