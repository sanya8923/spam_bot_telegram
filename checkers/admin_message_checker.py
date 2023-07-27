from checkers.message_checker import MessageChecker


class AdminMessageChecker(MessageChecker):
    def __init__(self, member, message: Message):
        super().__init__(message)
        self.member = member
        print('AdminMessageChecker')
