from aiogram.types import Message
from db.db_mongodb import db
from keyboards.choice_groups_keyboard import choice_groups_keyboard


async def check_membership_groups(update: Message):
    print('check_membership_groups')

    collection = db['group_user_role']
    documents = collection.find({'user_id': update.from_user.idd})
    documents_as_list = await documents.to_list(length=100)

    chat_names = []
    for document in documents_as_list:
        if document['role'] == 'creator' or 'administrator':
            chat_names.append(document['chat_name'])
    return await choice_groups_keyboard(chat_names)




