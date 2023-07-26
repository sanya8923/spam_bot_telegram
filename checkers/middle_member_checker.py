from checkers.member_checker import MemberChecker


class MiddleMemberChecker(MemberChecker):
    def __init__(self, member):
        self.member = member
