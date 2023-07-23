from db_saver import DbSaver
from data.data import UserData, GroupData, MessageData
from typing import Union
from data_manager.data_manager import DataManager
from db.db_mongodb import Db


class DbSaverUsers(DbSaver):
    async def save_to_db(self, obj: UserData) -> bool:
        print('save_to_db in DbSaverUsers')
        user_dict = await DataManager().get_data_to_dict(obj)
        await Db().update_data_one(user_dict)

