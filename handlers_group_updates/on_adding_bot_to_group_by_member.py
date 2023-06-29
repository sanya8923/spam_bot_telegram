from aiogram.types import ChatMemberUpdated


async def on_adding_bot_to_group_by_member(update: ChatMemberUpdated):
    print('bot added to group - member')