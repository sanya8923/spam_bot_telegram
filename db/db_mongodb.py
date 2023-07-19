import motor.motor_asyncio
import datetime
import config_reader
from typing import Optional, Union
from bot import bot

cluster = motor.motor_asyncio.AsyncIOMotorClient(config_reader.config.mongo_db.get_secret_value())
db = cluster['db']


async def add_data_to_db(collection_name, message_update):
    print('add_data_to_db')
    collection = db[collection_name]
    collection.insert_one(message_update)


async def get_membership_groups(user_id: int) -> list:
    print('check_membership_groups')

    collection_group_user_role = db['group_user_role']
    documents_user = collection_group_user_role.find({'user_id': user_id, 'role':
                                                     {'$in': ['administrator', 'creator']}})
    documents_bot = collection_group_user_role.find({'user_id': bot.id, 'role': 'administrator'})

    bot_chat_id_list = []
    async for document_bot in documents_bot:
        bot_chat_id_list.append(document_bot['chat_id'])
    bot_chat_id_set = set(bot_chat_id_list)

    user_chat_id_list = []
    async for document_user in documents_user:
        user_chat_id_list.append(document_user['chat_id'])
    user_chat_id_set = set(user_chat_id_list)

    chat_id_list = []
    for i in range(len(bot_chat_id_set)):
        for m in range(len(user_chat_id_set)):
            if list(bot_chat_id_set)[i] == list(user_chat_id_set)[m]:
                chat_id_list.append(list(bot_chat_id_set)[i])

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


async def get_user_role_from_db(user_id: int, chat_id: int) -> Union[int, None]:
    user = await db['group_user_role'].find_one({'user_id': user_id, 'chat_id': chat_id})
    if user:
        return user['role']
    else:
        return None


async def get_data_from_db(data_key: str, data_value: Union[str, list], col_name: str) -> Union[dict, list]:
    print('get_data_from_db')
    if type(data_value) == str:
        return await db[col_name].find_one({data_key: data_value})
    else:
        users_data = []
        for data in data_value:
            user = (await db[col_name].find_one({data_key: data}))
            users_data.append(user)
        return users_data


async def get_users_by_role(chat_id: int, role) -> list:
    cursor = db['group_user_role'].find({'chat_id': chat_id, 'role': role})
    return await cursor.to_list(length=100)


async def update_role_to_db(*args, **kwargs):
    print('update_role_to_db')
    chat_id = args[0]
    user_id = kwargs.get('user_id')
    user_data = kwargs.get('users_data')
    update = kwargs.get('update')
    message = kwargs.get('message')

    collection_name_group_user_role = 'group_user_role'
    collection_group_user_role = db[collection_name_group_user_role]

    if user_id:
        print('update_role_to_db FROM USER_ID')
        member = await bot.get_chat_member(chat_id, user_id)
        print(f'member: {member}')
        role = (await bot.get_chat_member(chat_id, user_id)).status
        count = await collection_group_user_role.count_documents({'user_id': user_id, 'chat_id': chat_id})
        user_role = {'user_id': user_id,
                     'chat_id': chat_id,
                     'role': role
                     }
        if count == 0:
            await add_data_to_db(collection_name_group_user_role, user_role)
        elif count == 1:
            filter_update = {'user_id': user_id, 'chat_id': chat_id}
            update_role = {'$set': {'role': user_role}}
            collection_group_user_role.update_one(filter_update, update_role)
        else:
            delete_filter = {'user_id': user_id, 'chat_id': chat_id}
            collection_group_user_role.delete_many(delete_filter)
            await add_data_to_db(collection_name_group_user_role, user_role)

    elif update:
        count = await collection_group_user_role.count_documents({'user_id': update.new_chat_member.user.id,
                                                                  'chat_id': update.chat.id})
        group_user_role = {'user_id': update.new_chat_member.user.id,
                           'username': update.new_chat_member.user.username,  # TODO: delete
                           'chat_id': update.chat.id,
                           'chat_name': update.chat.title,  # TODO: delete
                           'role': update.new_chat_member.status
                           }

        if count == 0:
            await add_data_to_db(collection_name_group_user_role, group_user_role)
        elif count == 1:
            filter_update = {'user_id': update.new_chat_member.user.id, 'chat_id': update.chat.id}
            update_role = {'$set': {'role': update.new_chat_member.status}}
            collection_group_user_role.update_one(filter_update, update_role)
        else:
            delete_filter = {'user_id': update.new_chat_member.user.id,
                             'chat_id': update.chat.id
                             }
            collection_group_user_role.delete_many(delete_filter)

            await add_data_to_db(collection_name_group_user_role, group_user_role)

    elif message:
        count = await collection_group_user_role.count_documents({'user_id': message.from_user.id,
                                                                  'chat_id': message.chat.id})

        role = (await bot.get_chat_member(message.chat.id, message.from_user.id)).status
        group_user_role = {'user_id': message.from_user.id,
                           'username': message.from_user.username,  # TODO: delete
                           'chat_id': message.chat.id,
                           'chat_name': message.chat.title,  # TODO: delete
                           'role': role
                           }

        if count == 0:
            await add_data_to_db(collection_name_group_user_role, group_user_role)
        elif count == 1:
            filter_update = {'user_id': message.from_user.id, 'chat_id': message.chat.id}
            update_db = {'$set': {'role': role}}
            collection_group_user_role.update_one(filter_update, update_db)
        else:
            delete_filter = {'user_id': message.from_user.id,
                             'chat_id': message.chat.id
                             }
            collection_group_user_role.delete_many(delete_filter)

            await add_data_to_db(collection_name_group_user_role, group_user_role)

    else:
        for line in user_data:
            count = await collection_group_user_role.count_documents({'user_id': line.user.id, 'chat_id': chat_id})
            user_role = {'user_id': line.user.id,
                         'username': line.user.username,
                         'chat_id': chat_id,
                         'chat_name': 'chat_name',
                         'role': line.status
                         }
            if count == 0:
                await add_data_to_db(collection_name_group_user_role, user_role)
            elif count == 1:
                filter_update = {'user_id': line.user.id, 'chat_id': chat_id}
                update_role = {'$set': {'role': line.status}}
                collection_group_user_role.update_one(filter_update, update_role)
            else:
                delete_filter = {'user_id': line.user.id, 'chat_id': chat_id}
                collection_group_user_role.delete_many(delete_filter)
                await add_data_to_db(collection_name_group_user_role, user_role)


async def save_user_to_db_users(chat_id: int, users_data: list):
    print('save_user_to_db_users')
    collection_user_name = 'users'
    collection_user = db[collection_user_name]

    for line in users_data:
        count = await collection_user.count_documents({'user_id': line.user.id})

        if count == 0:
            user = {'user_id': line.user.id,
                    'username': line.user.username,
                    'first_name': line.user.first_name,
                    'last_name': line.user.last_name
                    }
            await add_data_to_db(collection_user_name, user)
