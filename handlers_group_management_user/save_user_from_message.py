from aiogram.types import Message

from db.db_mongodb import add_data_to_db, check_user_exists_in_db, db


async def save_user_from_message(message: Message):
    collection_name = 'users'
    collection = db[collection_name]
    count = await collection.count_documents({'user_id': message.from_user.id})
    if count == 0:
        user = {
            'user_id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name
        }
        await add_data_to_db(collection_name, user)
