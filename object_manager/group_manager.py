from object_manager.object_manager import ObjManager


class GroupManager(ObjManager):
    def __init__(self, obj):
        self.object = obj

    async def check(self):
        print('check in GroupManager')
        pass