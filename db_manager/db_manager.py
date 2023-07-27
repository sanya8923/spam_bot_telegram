from db.db_mongodb import db


class DbManager:
    def __init__(self):
        self.db = db
