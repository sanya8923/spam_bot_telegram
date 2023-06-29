from aiogram.types import Message
from constants import DURATION_OF_NEW_USER_STATUS
from db.db_mongodb import db
from datetime import timedelta


async def check_new_member(message: Message) -> bool:
    new_member_pattern = message.date - timedelta(seconds=DURATION_OF_NEW_USER_STATUS)

    collection = db[f'{message.chat.id} - message updates']
    async for doc in collection.find(
            {'date_message': {'$gt': new_member_pattern}, 'user_id': message.from_user.id}):
        if doc.get('join_message'):
            return True
        else:
            return False




