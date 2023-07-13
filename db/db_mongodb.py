import motor.motor_asyncio
import datetime
import config_reader


cluster = motor.motor_asyncio.AsyncIOMotorClient(config_reader.config.mongo_db.get_secret_value())
db = cluster['db']


async def add_data_to_db(collection_name, message_update):
    print('add_data_to_db')
    collection = db[collection_name]
    collection.insert_one(message_update)


async def add_banned_member_to_collection(chat_id: int, user_id: int, date: datetime):
    collection = db[f'{chat_id} - banned members']
    data = {
        'user_id': user_id,
        'date_ban': date
    }
    collection.insert_one(data)


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


async def get_user_data(user_id: int) -> dict:
    return await db['users'].find_one({'user_id': user_id})
