from db.db_mongodb import Db
from data_manager.data_manager import DataManager
from aiogram.types import Message
from data.data import UserData, GroupData, MessageData
from typing import Union
from bot import bot
from db_saver_role import DbSaverRole
from db_saver_users import DbSaverUsers
from db_saver_groups import DbSaverGroups


class DbManager(Db):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.data = args[0]
        self._db: Db()
        self._data_manager: Union[None, DataManager] = None

    async def count(self, collection_name, key: str, value: int):
        print('count')
        collection = self._db[collection_name]
        return await collection.count_documents({f'{key}: {value}'})

    async def save_to_db(self, obj: Union[MessageData, UserData, GroupData]) -> bool:
        print('save_to_db in db_manager')

        check_user_db = await DbSaverUsers().save_to_db(obj.from_user)
        check_chat_db = await DbSaverGroups().save_to_db(obj.from_chat)
        check_message_db = await DbSaverRole().save_to_db(obj)




    # async def add_data_to_db(self, co):
    #     self._db = Db()
    #     self._data_manager = DataManager()
    #     dict = self._data_manager.set_data_to_dict(self.message)
    #     count = bot.documents
    #     await self.db.


    # async def on_user_data(self):
    #     print('on_user_data')
    #     if isinstance(self._db_result, list):
    #         if len(self._db_result) < 1:
    #             await self._db.add_data('users', self.dict)
    #
    # async def on_group_data(self):
    #     print('on_group_data')
    #     if isinstance(self._db_result, list):
    #         if len(self._db_result) < 1:
    #             await self._db.add_data('groups', self.dict)
    #             return True
    #         elif len(self._db_result) == 1:
    #             await self._db.update_data_one('groups', self.dict)
    #             return True
    #         else:
    #             await self._db.update_data_many('groups', self.dict)
    #             return True
    #     return False
    #
    # async def on_message_data(self):
    #     print('on_message_data')
    #     if isinstance(self._db_result, list):
    #         if len(self._db_result) < 1:
    #             await self._db.add_data('message_updates', self.dict)
    #             return True
    #         elif len(self._db_result) == 1:
    #             await self._db.update_data_one('groups', self.dict)
    #             return True
    #         else:
    #             await self._db.update_data_many('groups', self.dict)
    #             return True
    #     return False
