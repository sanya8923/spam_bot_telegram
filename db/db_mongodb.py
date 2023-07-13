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
