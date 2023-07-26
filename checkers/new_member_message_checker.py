from checkers.message_checker import MessageChecker


class NewMemberMessageChecker(MessageChecker):
    def __init__(self, member):
        self.member = member

    async def url_check(self):
        pass

    async def flood_check(self):
        pass

    async def ban_words_check(self):
        pass
