from abc import ABC, abstractmethod


class MemberChecker(ABC):
    def __init__(self, member):
        self.member = member

