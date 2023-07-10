from db.db_mongodb import db
from aiogram.types import ChatMemberUpdated


async def delete_chat_id_from_groups_db(update: ChatMemberUpdated):
    print('delete_chat_id_from_groups_db')
    # collection_name = 'groups'
    # collection = db[collection_name]
    #
    # count = collection.count_documents({'chat_id': update.chat.id})
    #
    # if count == 1:
    #     collection.delete_one({'chat_id': update.chat.id})
    # elif count > 1:
    #     collection.delete_many({'chat_id': update.chat.id})
    # else:
    #     raise ValueError("Chat ID don't exists")
