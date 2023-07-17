from aiogram.types import ChatMemberUpdated
from bot import bot
from db.db_mongodb import update_role_to_db, save_user_to_db_users


async def save_admins_to_db(update: ChatMemberUpdated):
    print('save_admins_to_db')
    admins_data = await bot.get_chat_administrators(update.chat.id)

    await update_role_to_db(update.chat.id, users_data=admins_data)
    await save_user_to_db_users(update.chat.id, users_data=admins_data)
