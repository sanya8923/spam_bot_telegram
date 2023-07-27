from checkers.message_checker import MessageChecker


class MiddleMemberMassageChecker(MessageChecker):
    def __init__(self, member):
        self.member = member
        print('MiddleMemberMassageChecker')
