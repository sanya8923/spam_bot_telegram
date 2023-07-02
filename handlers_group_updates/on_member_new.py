from aiogram.types import ChatMemberUpdated
from db.update_users_db_from_member_update import update_users_db_from_member_update
from db.update_group_user_role_db import update_group_user_role_db


async def on_member_new(update: ChatMemberUpdated):
    print('on_new_member')
    await update_users_db_from_member_update(update)
    await update_group_user_role_db(update)
