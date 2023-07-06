from aiogram.types import ChatMemberUpdated
from db.save_admins_to_db import save_admins_to_db
from db.save_group_to_db import save_group_to_db


async def on_bot_add_by_admin(update: ChatMemberUpdated):
    print('bot added to group - admin')

    await save_admins_to_db(update)
    await save_group_to_db(update)
