from aiogram.types import Message
from db.db_mongodb import db

# TODO: пойми нахуя и доделай. Логика в этом есть
async def save_group_user_role(message: Message):
    collection_name = 'group_user_role'
    collection = db[collection_name]
    count = await collection.count_documents({'user_id': message.from_user.id})

    if count == 0:
        group_user_role = {
            'user_id': message.from_user.id,
            'chat_id': message.chat.id,
            'role': None,
            'is_bot': None
        }
    elif count == 1:
        pass
    else:
        print('In db "group_user_role" ')
    return 0