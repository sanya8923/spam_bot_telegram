import motor.motor_asyncio
import datetime
from constants import TIME_SPAN_TO_CHECK_NUMBER_OF_MESSAGES_MIN, ALLOWED_NUMBER_OF_MESSAGE_FOR_PERIOD
from aiogram.types import Message


cluster = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://sanya8923:17XS7eoFcAtELvlx@cluster0.lzxiped.mongodb.net/db?retryWrites=true&w=majority')
db = cluster['db']


async def print_list_collection_names():
    collection_names = await db.list_collection_names()
    for name in collection_names:
        print(name)


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


async def remove_group_id_where_bot_is_no_longer_member(chat_id: int):
    collection = db['groups']
    collection.delete_one({'member': chat_id})




