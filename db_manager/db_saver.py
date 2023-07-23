from abc import ABC, abstractmethod
from data.data import UserData, GroupData, MessageData
from typing import Union


class DbSaver(ABC):
    @abstractmethod
    async def save_to_db(self, obj: Union[MessageData, UserData, GroupData]) -> bool:
        pass
