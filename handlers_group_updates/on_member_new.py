from aiogram.types import ChatMemberUpdated
from handlers_group_management_user.save_user import save_user
from handlers_group_management_user.update_group_user_role import update_group_user_role


async def on_member_new(update: ChatMemberUpdated):
    print('on_new_member')
    await save_user(update)
    await update_group_user_role(update, 'member')
