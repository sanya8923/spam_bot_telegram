from aiogram.types import ChatMemberUpdated
from db.db_mongodb import db


async def update_group_user_role_db(update: ChatMemberUpdated, role: str):
    chat_id = update.chat.id
    user_id = update.from_user.id

    collection_name = 'group_user_role'
    collection = db[collection_name]

    print('update_group_user_role_db')

    collection.update_one({'user_id': user_id, 'chat_id': chat_id}, {'$set': {'role': role}})
