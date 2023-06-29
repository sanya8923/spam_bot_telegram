from aiogram.types import ChatMemberUpdated
from db.db_mongodb import add_group_where_bot_is_member


async def on_adding_bot_to_group_by_member(update: ChatMemberUpdated):
    print('bot added to group - member')
    chat_id = update.chat.id
    await add_group_where_bot_is_member(chat_id)
