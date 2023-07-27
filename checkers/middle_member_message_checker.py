from checkers.message_checker import MessageChecker


class MiddleMemberMassageChecker(MessageChecker):
    def __init__(self, member, message: Message):
        super().__init__(message)
        self.member = member
        print('MiddleMemberMassageChecker')
