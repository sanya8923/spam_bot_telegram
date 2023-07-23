from abc import ABC, abstractmethod
from aiogram.types import Message
from data.data import UserData, GroupData, MessageData
from typing import Union


class DataConverter(ABC):
    @abstractmethod
    async def get_data_to_dict(self, obj: Union[UserData, GroupData, MessageData]):
        pass

    @abstractmethod
    async def save_message(self, message: Message):
        pass
