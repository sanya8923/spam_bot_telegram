from checkers.message_checker import MessageChecker


class NewMemberMessageChecker(MessageChecker):
    def __init__(self, member):
        self.member = member

    async def url_check(self):
        pass


