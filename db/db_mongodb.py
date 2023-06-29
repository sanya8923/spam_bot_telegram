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


async def add_message_update_to_collection(message_update):
    collection = db[f'{message_update.chat_id} - message updates']
    data = {
        'date_message': message_update.date_message,
        'message_id': message_update.message_id,
        'user_id': message_update.user_id,
        'join_message': message_update.join_message
    }
    collection.insert_one(data)


async def add_banned_member_to_collection(chat_id: int, user_id: int, date: datetime):
    collection = db[f'{chat_id} - banned members']
    data = {
        'user_id': user_id,
        'date_ban': date
    }
    collection.insert_one(data)


async def add_group_where_bot_is_member(chat_id: int):
    collection = db['group_where_bot_is_member']
    data = {
        'chat_id': chat_id
    }
    collection.insert_one(data)



