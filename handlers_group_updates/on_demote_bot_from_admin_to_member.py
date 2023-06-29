from aiogram.types import ChatMemberUpdated


async def on_demote_bot_from_admin_to_member(update: ChatMemberUpdated):
    print('bot demote from admin to member')
