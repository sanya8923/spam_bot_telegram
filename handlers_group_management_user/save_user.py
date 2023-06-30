from aiogram.types import Message

from db.db_mongodb import add_data_to_db, check_user_exists_in_db, db


class User:
    id: int
    username: str
    first_name: str
    last_name: str


async def save_user(message: Message):
    collection_name = 'users'
    collection = db[collection_name]
    count = await collection.count_documents({'id': message.from_user.id})
    print(f'count in save_user: {count}')
    if count == 0:
        user = {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name
        }
        await add_data_to_db(collection_name, user)
