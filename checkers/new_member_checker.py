from checkers.member_checker import MemberChecker


class NewMemberChecker(MemberChecker):
    def __init__(self, member):
        self.member = member

    async def check(self):
        pass
