from bot import bot
from db.db_mongodb import db, add_data_to_db


async def save_group_admins(chat_id):
    collection_name = 'group_user_role'
    admins_data = await bot.get_chat_administrators(chat_id)

    for line in admins_data:
        if line.status == 'administrator':
            admin = {'user_id': line.user.id,
                     'chat_id': chat_id,
                     'role': 'administrator'
                     }
            await add_data_to_db(collection_name, admin)
        elif line.status == 'creator':
            creator = {'user_id': line.user.id,
                       'chat_id': chat_id,
                       'role': 'creator'
                       }
            await add_data_to_db(collection_name, creator)
