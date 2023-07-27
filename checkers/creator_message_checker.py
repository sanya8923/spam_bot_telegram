from checkers.message_checker import MessageChecker


class CreatorMessageChecker(MessageChecker):
    def __init__(self, member):
        self.member = member
        print('CreatorMessageChecker')
