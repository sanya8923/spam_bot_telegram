from abc import ABC, abstractmethod


class DataConverter(ABC):
    @abstractmethod
    async def get_data_to_dict(self):
        pass