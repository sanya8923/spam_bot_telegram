from aiogram.types import Message
from abc import ABC, abstractmethod


class MessageChecker(ABC):
    def __init__(self, message: Message):
        self.message = message

    @abstractmethod
    async def url_check(self):
        pass

    @abstractmethod
    async def flood_check(self):
        pass

    @abstractmethod
    async def ban_words_check(self):
        pass
