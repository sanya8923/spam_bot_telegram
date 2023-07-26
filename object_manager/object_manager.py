from abc import ABC, abstractmethod


class ObjManager(ABC):
    def __init__(self, obj):
        self.object = obj

    @abstractmethod
    async def check(self):
        pass
