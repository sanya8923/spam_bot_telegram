from aiogram.types import ChatMemberUpdated
from db.db_mongodb import db
from db.db_mongodb import add_data_to_db


async def update_group_user_role_db(update: ChatMemberUpdated):

    collection_name = 'group_user_role'
    collection = db[collection_name]
    count = await collection.count_documents({'user_id': update.new_chat_member.user.id, 'chat_id': update.chat.id})
    group_user_role = {'user_id': update.new_chat_member.user.id,
                       'username': update.new_chat_member.user.username,
                       'chat_id': update.chat.id,
                       'role': update.new_chat_member.status
                       }

    if count == 0:
        await add_data_to_db(collection_name, group_user_role)
    elif count == 1:
        filter_update = {'user_id': update.new_chat_member.user.id, 'chat_id': update.chat.id}
        update = {'$set': {'role': update.new_chat_member.status}}
        collection.update_one(filter_update, update)
    else:
        delete_filter = {'user_id': update.new_chat_member.user.id,
                         'chat_id': update.chat.id
                         }
        collection.delete_many(delete_filter)

        await add_data_to_db(collection_name, group_user_role)



