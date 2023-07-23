from aiogram.types import Message
from db.db_mongodb import Db


async def update_users_db_from_message(message: Message):
    print('update_users_db_from_message')
    # db = Db()
    # collection_name = 'users'
    # collection = db[collection_name]
    # count = await collection.count_documents({'user_id': message.from_user.id})
    # user = {
    #     'user_id': message.from_user.id,
    #     'username': message.from_user.username,
    #     'first_name': message.from_user.first_name,
    #     'last_name': message.from_user.last_name
    # }
    #
    # if count == 0:
    #     await db.add_data(collection_name, user)
    # elif count > 1:
    #     delete_filter = {'user_id': message.from_user.id}
    #     collection.delete_many(delete_filter)
    #
    #     await db.add_data(collection_name, user)

