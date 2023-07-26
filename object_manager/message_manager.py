from object_manager.object_manager import ObjManager


class MessageManager(ObjManager):
    def __init__(self, obj):
        self.object = obj

    async def check(self):
        print('check in MessageManager')
        return 0
