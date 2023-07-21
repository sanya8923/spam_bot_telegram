from my_router import MyRouter
from db_manager.db_manager import DbManager


class DataTypeRouter(MyRouter):
    def __init__(self, *args, **kwargs):
        self.data = args[0]
        self.db_manager = DbManager()

    async def run(self):
        print('DataTypeRouter')
        try:
            if self.data.type == 'user_data':
                await self.db_manager.on_user_data(self.data)
            elif self.data.type == 'message_data':
                await self.db_manager.on_message_data(self.data)
            elif self.data.type == 'group_data':
                await self.db_manager.on_group_data(self.data)
            else:
                return False
        except TypeError as e:
            raise TypeError  # TODO: add except
