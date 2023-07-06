from aiogram.types import ChatMemberUpdated


async def on_bot_member_left(update: ChatMemberUpdated):
    print('bot-member left group')
