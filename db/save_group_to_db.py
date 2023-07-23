from aiogram.types import ChatMemberUpdated

from db.db_mongodb import Db


async def save_group_to_db(update: ChatMemberUpdated):
    print('save_group_to_db')
    db = Db
    collection_name = 'groups'
    collection = db[collection_name]

    count = await collection.count_documents({'chat_id': update.chat.id})
    if count == 0:
        group = {
            'chat_id': update.chat.id,
            'chat_username': update.chat.username,
            'chat_name': update.chat.title
        }
        await db.add_data(collection_name, group)

