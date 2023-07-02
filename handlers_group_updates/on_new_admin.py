from aiogram.types import ChatMemberUpdated
from handlers_group_updates.update_group_user_role_db import update_group_user_role_db


async def on_new_admin(update: ChatMemberUpdated):
    print('on_new_admin')
    await update_group_user_role_db(update, 'administrator')
