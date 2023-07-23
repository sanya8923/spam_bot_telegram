from db_saver import DbSaver
from data.data import UserData, GroupData, MessageData
from typing import Union


class DbSaverGroups(DbSaver):
    async def save_to_db(self, obj: GroupData) -> bool:
        pass