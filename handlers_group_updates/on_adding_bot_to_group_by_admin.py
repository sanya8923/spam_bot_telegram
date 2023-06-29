from aiogram.types import ChatMemberUpdated
from db.db_mongodb import add_group_id_where_bot_is_admin


async def on_adding_bot_to_group_by_admin(update: ChatMemberUpdated):
    print('bot added to group - admin')
    chat_id = update.chat.id
    await add_group_id_where_bot_is_admin(chat_id)
