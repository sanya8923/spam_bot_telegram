from checkers.message_checker import MessageChecker
from aiogram.types import Message, User


class CreatorMessageChecker(MessageChecker):
    def __init__(self, message: Message):
        super().__init__(message)
        self.message = message
        self.member = self.message.from_user
        print('CreatorMessageChecker')
