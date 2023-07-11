from aiogram.types import ChatMemberUpdated
from bot import bot
from db.db_mongodb import db, add_data_to_db


async def save_admins_to_db(update: ChatMemberUpdated):
    print('save_admins_to_db')
    admins_data = await bot.get_chat_administrators(update.chat.id)

    collection_name_group_user_role = 'group_user_role'
    collection_group_user_role = db[collection_name_group_user_role]

    for admin in admins_data:
        count = await collection_group_user_role.count_documents({'user_id': admin.user.id, 'chat_id': update.chat.id})
        user_role = {'user_id': admin.user.id,
                     'username': admin.user.username,
                     'chat_id': update.chat.id,
                     'chat_name': update.chat.title,
                     'role': admin.status
                     }
        if count == 0:
            await add_data_to_db(collection_name_group_user_role, user_role)
        elif count == 1:
            filter_update = {'user_id': admin.user.id, 'chat_id': update.chat.id}
            update_user = {'$set': {'role': admin.status}}
            collection_group_user_role.update_one(filter_update, update_user)
        else:
            delete_filter = {'user_id': admin.user.id, 'chat_id': update.chat.id}
            collection_group_user_role.delete_many(delete_filter)
            await add_data_to_db(collection_name_group_user_role, user_role)

        collection_user_name = 'users'
        collection_user = db[collection_user_name]
        count = await collection_user.count_documents({'user_id': admin.user.id})

        if count == 0:
            user = {'user_id': admin.user.id,
                    'username': admin.user.username,
                    'first_name': admin.user.first_name,
                    'last_name': admin.user.last_name
                    }
            await add_data_to_db(collection_user_name, user)
