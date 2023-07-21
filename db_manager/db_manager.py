class DbManager:
    def __init__(self, *args, **kwargs):
        self.data = args[0]

    async def qualifier(self):
        pass

    async def on_user_data(self):
        pass

    async def on_group_data(self):
        pass

    async def on_message_data(self):
        pass

    async def router(self):
        db_manager = DbManager(self.data)
        try:
            if db_manager == 'user':
                await db_manager.on_user_data()
            elif db_manager == 'group':
                await db_manager.on_group_data()
            elif db_manager == 'message':
                await db_manager.on_message_data()
        except None # TODO: add except


