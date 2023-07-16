import motor.motor_asyncio
import datetime
import config_reader
from typing import Optional, Union


cluster = motor.motor_asyncio.AsyncIOMotorClient(config_reader.config.mongo_db.get_secret_value())
db = cluster['db']


async def add_data_to_db(collection_name, message_update):
    print('add_data_to_db')
    collection = db[collection_name]
    collection.insert_one(message_update)


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
            chats_data.append(
                {
                    'chat_name': document['chat_name'],
                    'chat_username': document['chat_username'],
                    'chat_id': document['chat_id']
                }
            )

    return chats_data


async def get_user_role(user_id: int, chat_id: int) -> str:
    return (await db['group_user_role'].find_one({'user_id': user_id, 'chat_id': chat_id}))['role']


async def get_user_data(user_data_key: str, user_data_value: Union[str, list]) -> Union[dict, list]:
    if type(user_data_value) == str:
        return await db['users'].find_one({user_data_key: user_data_value})
    else:
        users_data = []
        for data in user_data_value:
            user = (await db['users'].find_one({user_data_key: data}))
            users_data.append(user)
        return users_data


async def get_users_by_role(chat_id: int, role) -> list:
    cursor = db['group_user_role'].find({'chat_id': chat_id, 'role': role})
    return await cursor.to_list(length=100)

