from checkers.message_checker import MessageChecker


class MiddleMemberChecker(MessageChecker):
    def __init__(self, member):
        self.member = member


