from aiogram.types import ChatMemberUpdated


async def on_left_bot_member_from_group(update: ChatMemberUpdated):
    print('bot-member left group')
