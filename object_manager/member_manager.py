from object_manager.object_manager import ObjManager


class MemberManager(ObjManager):
    def __init__(self, obj):
        self.object = obj

    async def check(self):
        print('check in MemberManager')
        pass

    async def get_status_member(self):
        pass
