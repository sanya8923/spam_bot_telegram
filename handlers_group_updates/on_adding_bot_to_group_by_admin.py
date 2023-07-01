from aiogram.types import ChatMemberUpdated
from db.db_mongodb import remove_group_id_where_bot_is_no_longer_member
from handlers_group_management_user.save_group_admins import save_group_admins


async def on_adding_bot_to_group_by_admin(update: ChatMemberUpdated):
    print('bot added to group - admin')
    chat_id = update.chat.id
    await save_group_admins(chat_id)
    await remove_group_id_where_bot_is_no_longer_member(chat_id)
