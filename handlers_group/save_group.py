from aiogram.types import Message

from db.db_mongodb import db, add_data_to_db


async def save_group(message: Message):
    collection_name = 'groups'
    collection = db[collection_name]

    count = await collection.count_documents({'group_id': message.chat.id})
    if count == 0:
        group = {
            'group_id': message.chat.id
        }
        await add_data_to_db(collection_name, group)

