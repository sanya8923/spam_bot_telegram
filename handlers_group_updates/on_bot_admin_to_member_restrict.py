from aiogram.types import ChatMemberUpdated


async def on_bot_admin_to_member_restrict(update: ChatMemberUpdated):
    print('bot demote from admin to member')
