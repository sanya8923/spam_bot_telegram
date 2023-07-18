from aiogram.types import Message
from db.db_mongodb import db, add_data_to_db, get_user_role_from_db


async def update_group_user_role_db(message: Message):
    print('update_group_user_role_db')
    collection_name = 'group_user_role'
    collection = db[collection_name]
    role = await get_user_role_from_db(message)
    count = await collection.count_documents({'user_id': message.from_user.id, 'chat_id': message.chat.id})

    if await collection.find_one({'user_id': message.from_user.id, 'chat_id': message.chat.id}):
        role_from_db = (await collection.find_one({'user_id': message.from_user.id, 'chat_id': message.chat.id}))['role']

    group_user_role = {'user_id': message.from_user.id,
                       'username': message.from_user.username,  # TODO: delete
                       'chat_id': message.chat.id,
                       'chat_name': message.chat.title,  # TODO: delete
                       'role': role
                       }

    if count == 0:
        await add_data_to_db(collection_name, group_user_role)
    elif count == 1 and role != role_from_db:
        filter_update = {'user_id': message.from_user.id, 'chat_id': message.chat.id}
        update = {'$set': {'role': role}}
        collection.update_one(filter_update, update)
    else:
        print('user in db and role is correct')



