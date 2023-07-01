from bot import bot
from db.db_mongodb import db, add_data_to_db


async def save_group_admins(chat_id):
    admins_data = await bot.get_chat_administrators(chat_id)
    collection_user = db['users']

    for line in admins_data:
        if line.status == 'administrator':
            admin = {'user_id': line.user.id,
                     'username': line.user.username,
                     'chat_id': chat_id,
                     'role': 'administrator'
                     }
            await add_data_to_db('group_user_role', admin)
        elif line.status == 'creator':
            creator = {'user_id': line.user.id,
                       'username': line.user.username,
                       'chat_id': chat_id,
                       'role': 'creator'
                       }
            await add_data_to_db('group_user_role', creator)

        count = await collection_user.count_documents({'user_id': line.user.id})

        if count == 0:
            user = {'user_id': line.user.id,
                    'username': line.user.username,
                    'first_name': line.user.first_name,
                    'last_name': line.user.last_name
                    }
            await add_data_to_db('users', user)
