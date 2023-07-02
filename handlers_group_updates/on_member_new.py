from aiogram.types import ChatMemberUpdated
from handlers_group_management_user.save_user import save_user
from handlers_group_updates.update_group_user_role_db import update_group_user_role_db


async def on_member_new(update: ChatMemberUpdated):
    print('on_new_member')
    await save_user(update)
    await update_group_user_role_db(update)
