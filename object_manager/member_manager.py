from object_manager.object_manager import ObjManager


class MemberManager(ObjManager):
    def __init__(self, member):
        self.member = member

    async def check(self):
        print('check in MemberManager')
        pass

    async def get_status_member(self):
        print('get_status_member in MemberManager')
        pass
