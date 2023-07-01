from aiogram.types import ChatMemberUpdated


async def on_add_bot_by_member(update: ChatMemberUpdated):
    print('bot added to group - member')

