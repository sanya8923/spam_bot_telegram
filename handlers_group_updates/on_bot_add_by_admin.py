from aiogram.types import ChatMemberUpdated
from db.db_mongodb import remove_group_id_where_bot_is_no_longer_member
from handlers_group_management_user.save_group_admins import save_group_admins
from handlers_group.save_group import save_group


async def on_bot_add_by_admin(update: ChatMemberUpdated):
    print('bot added to group - admin')

    await save_group_admins(update.chat.id)
    await save_group(update)
    # await remove_group_id_where_bot_is_no_longer_member(chat_id)
