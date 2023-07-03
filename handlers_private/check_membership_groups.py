from aiogram.types import Message
from db.db_mongodb import db
from keyboards.choice_groups_keyboard import choice_groups_keyboard


async def check_membership_groups(update: Message):
    print('check_membership_groups')
    user_id = update.from_user.id

    collection = db['group_user_role']

    documents = collection.find({'user_id': user_id})


    documents_as_list = await documents.to_list(length=100)
    for document in documents_as_list:
        if document['role'] == 'creator' or 'administrator':
            groups_id = document['chat_id']




