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

    async def on_user_data(self):
        print('on_user_data')
        if isinstance(self._db_result, list):
            if len(self._db_result) < 1:
                await self._db.add_data('users', self.dict)

    async def on_group_data(self):
        print('on_group_data')
        if isinstance(self._db_result, list):
            if len(self._db_result) < 1:
                await self._db.add_data('groups', self.dict)
                return True
            elif len(self._db_result) == 1:
                await self._db.update_data_one('groups', self.dict)
                return True
            else:
                await self._db.update_data_many('groups', self.dict)
                return True
        return False


