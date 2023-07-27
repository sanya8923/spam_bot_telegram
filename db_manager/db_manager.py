from db.db_mongodb import db
from aiogram.types import Message


class DbManager:
    def __init__(self, message: Message):
        self.db = db
