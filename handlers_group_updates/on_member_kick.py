from aiogram.types import ChatMemberUpdated
from db.update_group_user_role_db import update_group_user_role_db


async def on_member_kick(update: ChatMemberUpdated):
    await update_group_user_role_db(update)
