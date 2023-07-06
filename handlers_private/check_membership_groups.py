from aiogram.types import Message
from db.db_mongodb import db
from keyboards.choice_groups_keyboard import choice_groups_keyboard


async def check_membership_groups(update: Message):
    print('check_membership_groups')

    collection_group_user_role = db['group_user_role']
    documents_group_user_role = collection_group_user_role.find({'user_id': update.from_user.id})

    chat_id_list = []
    async for document in documents_group_user_role:
        chat_id_list.append(document['chat_id'])

    collection_groups = db['groups']
    chat_data = []

    for chat_id in chat_id_list:
        documents_groups = collection_groups.find({f'chat_id': chat_id})
        async for document in documents_groups:
            chat_data.append((document['chat_name'], document['chat_username']))
            print(f'chat_data: {chat_data}')
            await choice_groups_keyboard(update, chat_data)






