from checkers.message_checker import MessageChecker


class AdminMessageChecker(MessageChecker):
    def __init__(self, member):
        self.member = member
        print('AdminMessageChecker')
