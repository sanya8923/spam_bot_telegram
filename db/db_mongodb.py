import motor.motor_asyncio


cluster = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://sanya8923:17XS7eoFcAtELvlx@cluster0.lzxiped.mongodb.net/db?retryWrites=true&w=majority')
db = cluster['db']


async def print_list_collection_names():
    collection_names = await db.list_collection_names()
    for name in collection_names:
        print(name)


async def add_message_update_to_collection(message_update):
    collection = db[str(message_update.chat_id)]
    data = {
        'date_message': message_update.date_message,
        'message_id': message_update.message_id,
        'user_id': message_update.user_id,
        'join_message': message_update.join_message
    }
    collection.insert_one(data)





