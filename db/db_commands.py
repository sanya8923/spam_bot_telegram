import aioredis
from db import db


async def set_data(name: str, val: str):
    await db.set(name=name, value=val)


async def get_data(name: str):
    return await db.get(name=name)


async def add_message_update(message_update):
    chat_id_key = str(message_update.chat_id)
    message_id_key = str(message_update.message_id)

    message_hash = {
        'user_id': str(message_update.user_id),
        'date_message': str(message_update.date_message),
        'join_message': str(message_update.join_message)
    }

    await db.hset(chat_id_key, message_id_key, message_hash)

