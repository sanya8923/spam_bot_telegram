from aiogram.types import ChatMemberUpdated
from db.db_mongodb import add_data_to_db, db


async def update_users_db_from_member_update(update: ChatMemberUpdated):
    print('update_users_db_from_member_update')
    collection_name = 'users'
    collection = db[collection_name]
    count = await collection.count_documents({'user_id': update.new_chat_member.user.id})
    user = {
        'user_id': update.new_chat_member.user.id,
        'username': update.new_chat_member.user.username,
        'first_name': update.new_chat_member.user.first_name,
        'last_name': update.new_chat_member.user.last_name
    }

    if count == 0:
        await add_data_to_db(collection_name, user)
    elif count > 1:
        delete_filter = {'user_id': update.new_chat_member.user.id}
        collection.delete_many(delete_filter)

        await add_data_to_db(collection_name, user)

