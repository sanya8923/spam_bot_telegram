from bot import bot
from aiogram.types import Message
from db.db_mongodb import db


async def get_user_role(message: Message):
    print('get_user_role')
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    return user.status


async def get_membership_groups(user_id: int) -> list:
    print('check_membership_groups')

    collection_group_user_role = db['group_user_role']
    documents_group_user_role = collection_group_user_role.find({'user_id': user_id})

    chat_id_list = []
    async for document in documents_group_user_role:
        chat_id_list.append(document['chat_id'])

    collection_groups = db['groups']
    chats_data = []

    for chat_id in set(chat_id_list):
        documents_groups = collection_groups.find({f'chat_id': chat_id})
        async for document in documents_groups:
            chats_data.append((document['chat_name'], document['chat_username'], document['chat_id']))

    return chats_data
