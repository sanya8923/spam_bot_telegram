from aiogram.types import ChatMemberUpdated
from db.db_mongodb import remove_group_id_where_bot_is_no_longer_member


async def on_adding_bot_to_group_by_admin(update: ChatMemberUpdated):
    print('bot added to group - admin')
    chat_id = update.chat.id
    # await add_chat_id_to_collection(chat_id, True)
    await remove_group_id_where_bot_is_no_longer_member(chat_id)
