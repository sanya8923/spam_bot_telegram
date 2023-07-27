from object_manager.object_manager import ObjManager
from bot import bot
from aiogram.types import Message
from db.db_mongodb import db
from datetime import timedelta
from constants import DURATION_OF_NEW_USER_STATUS
from pymongo.errors import PyMongoError, ServerSelectionTimeoutError, ConnectionFailure, OperationFailure


class MemberManager(ObjManager):
    def __init__(self, message: Message):
        self.message = message
        self.member = self.message.from_user
        self.group = self.message.chat

    async def get_status_member(self) -> str:
        print('get_status_member in MemberManager')
        try:
            user = await bot.get_chat_member(self.group.id, self.member.id)
            status = user.status
            if status == 'member':
                new_member_pattern = self.message.date - timedelta(seconds=DURATION_OF_NEW_USER_STATUS)

                collection = db[f'{self.group.id} - messages_updates']
                async for doc in collection.find(
                        {'date_message': {'$gt': new_member_pattern}, 'user_id': self.member.id}):
                    print(f'doc: {doc}')
                    if doc.get('join_message'):
                        status = 'new_member'
                    else:
                        status = 'middle_member'
        except (PyMongoError, ServerSelectionTimeoutError, ConnectionFailure, OperationFailure) as e:
            if isinstance(e, OperationFailure):
                print(f"TypeError: {e}")
                print(f"Current object: {self}")
            elif isinstance(e, ServerSelectionTimeoutError):
                print(f"TypeError: {e}")
                print(f"Current object: {self}")
            elif isinstance(e, ConnectionFailure):
                print(f"TypeError: {e}")
                print(f"Current object: {self}")
            else:
                print(f"TypeError: {e}")
                print(f"Current object: {self}")
        return status

    async def check(self):
        print('check in MemberManager')
