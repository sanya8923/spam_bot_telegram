from aiogram.types import Message
from db.db_mongodb import db
from texts_of_message import text_choice_group
from keyboards.choice_groups_inline_keyboard import choice_groups_inline_keyboard


async def check_membership_groups(message: Message):
    print('check_membership_groups')

    collection_group_user_role = db['group_user_role']
    documents_group_user_role = collection_group_user_role.find({'user_id': message.from_user.id})

    chat_id_list = []
    async for document in documents_group_user_role:
        chat_id_list.append(document['chat_id'])

    collection_groups = db['groups']
    chat_data = []

    for chat_id in set(chat_id_list):
        documents_groups = collection_groups.find({f'chat_id': chat_id})
        async for document in documents_groups:
            chat_data.append((document['chat_name'], document['chat_username'], document['chat_id']))

    return chat_data






