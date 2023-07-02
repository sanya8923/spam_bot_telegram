from aiogram.types import ChatMemberUpdated
from handlers_group_management_user.update_users_db import update_users_db
from handlers_group_updates.update_group_user_role_db import update_group_user_role_db


async def on_member_new(update: ChatMemberUpdated):
    print('on_new_member')
    await update_users_db(update)
    await update_group_user_role_db(update)
