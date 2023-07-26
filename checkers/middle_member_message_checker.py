from checkers.message_checker import MessageChecker


class MiddleMemberMassageChecker(MessageChecker):
    def __init__(self, member):
        self.member = member

    async def url_check(self):
        print(f'url_check in MiddleMemberMassageChecker: {url_check}')
        pass

    async def flood_check(self):
        print(f'flood_check in MiddleMemberMassageChecker: {flood_check}')
        pass

    async def ban_words_check(self):
        print(f'ban_words_check in MiddleMemberMassageChecker:{ban_words_check}')
        pass
