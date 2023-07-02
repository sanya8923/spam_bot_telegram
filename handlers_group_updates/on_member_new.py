from aiogram.types import ChatMemberUpdated
from handlers_group_management_user.save_user import save_user


async def on_member_new(update: ChatMemberUpdated):
    print('on_new_member')
    await save_user(update)
