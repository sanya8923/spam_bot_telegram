from abc import ABC, abstractmethod


class ObjectManager(ABC):
    def __init__(self, obj):
        self.object = obj

    @abstractmethod
    async def check(self):
        pass
