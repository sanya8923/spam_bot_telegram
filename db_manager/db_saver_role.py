from db_saver import DbSaver
from data.data import UserData, GroupData, MessageData
from typing import Union


class DbSaverRole(DbSaver):
    async def save_to_db(self, obj: Union[MessageData, UserData, GroupData]) -> bool:
        pass
