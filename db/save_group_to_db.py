from aiogram.types import ChatMemberUpdated

from db.db_mongodb import db, add_data_to_db


async def save_group_to_db(update: ChatMemberUpdated):
    collection_name = 'groups'
    collection = db[collection_name]

    count = await collection.count_documents({'group_id': update.chat.id})
    if count == 0:
        group = {
            'chat_id': update.chat.id,
            'chat_username': update.chat.username,
            'chat_name': update.chat.title
        }
        await add_data_to_db(collection_name, group)

