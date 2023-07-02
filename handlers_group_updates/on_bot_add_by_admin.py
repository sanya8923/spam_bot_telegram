from aiogram.types import ChatMemberUpdated
from db.save_group_admins import save_group_admins
from db.save_group_to_db import save_group_to_db


async def on_bot_add_by_admin(update: ChatMemberUpdated):
    print('bot added to group - admin')

    await save_group_admins(update.chat.id)
    await save_group_to_db(update)
    # await remove_group_id_where_bot_is_no_longer_member(chat_id)
