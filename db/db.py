import json

from redis import asyncio as aioredis


db = aioredis.from_url('redis://localhost', encoding="utf-8", decode_responses=True)


async def set_data(name: str, val: str):
    await db.set(name=name, value=val)


async def get_message_data(message_id_key):
    chat_ids = await db.keys("chat_id:*")
    for chat_id_key in chat_ids:
        message_data_json = await db.hget(chat_id_key, message_id_key)
        if message_data_json is not None:
            message_data = json.loads(message_data_json)
            user_id = int(message_data["user_id"])
            date_message = int(message_data["date_message"])
            join_message = bool(message_data["join_message"])
            return user_id, date_message, join_message
    return None, None, None


async def add_message_update(message_update):
    print('add_message_update: working')
    chat_id_key = str(message_update.chat_id)
    message_id_key = str(message_update.message_id)

    message_json = json.dumps(
        {
            'user_id': str(message_update.user_id),
            'date_message': str(message_update.date_message),
            'join_message': str(message_update.join_message)
        }
    )
    # message_hash_json = json.dumps(message_hash)

    await db.hset(chat_id_key, message_id_key, message_json)


async def add_message_update2(message_update):
    chat_id_key = f'chat_id: {message_update.chat_id}'
    message_id = message_update.message_id

    message_data = {
        'user_id': str(message_update.user_id),
        'date_message': str(message_update.date_message),
        'join_message': str(message_update.join_message)
    }
    message_json = json.dumps(message_data)

    await db.zadd(chat_id_key, {'message_id': message_update.message_id})
    await db.hset(message_id, mapping=message_data)


async def get_message_data2(chat_id):
    chat_id_key = f"chat_id:{chat_id}"

    # Получаем все сообщения для данного chat_id в отсортированном порядке
    message_ids = await db.zrange(chat_id_key, 0, -1)  # здесь пусто! проблема здесь

    message_data = []
    for message_id in message_ids:
        # Получаем данные о каждом сообщении из хэша
        message_json = await db.hget(message_id, 'message_data')
        if message_json is not None:
            message_data.append(json.loads(message_json))

    return message_data

