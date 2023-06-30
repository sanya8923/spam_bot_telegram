from aiogram.types import ChatMemberUpdated


async def on_adding_bot_to_group_by_member(update: ChatMemberUpdated):
    print('bot added to group - member')
    chat_id = update.chat.id
    # await add_chat_id_to_collection(chat_id, False)
