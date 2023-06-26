import motor.motor_asyncio


cluster = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://sanya8923:17XS7eoFcAtELvlx@cluster0.lzxiped.mongodb.net/db?retryWrites=true&w=majority')
collection = cluster.db.spam_bot


async def add_message_update_to_collection(message_update):

