from aiogram.types import ChatMemberUpdated
from db.update_group_user_role_db import update_group_user_role_db


async def on_admin_restrict_to_member(update: ChatMemberUpdated):
    await update_group_user_role_db(update)
