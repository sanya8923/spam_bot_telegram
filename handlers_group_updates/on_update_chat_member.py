from aiogram import Router
from aiogram.types import ChatMemberUpdated
from handlers_group_updates.on_member_new import on_member_new
from handlers_group_updates.on_admin_new import on_admin_new
from handlers_group_updates.on_admin_restrict_to_member import on_admin_restrict_to_member
from handlers_group_updates.on_admin_kick import on_admin_kick
from handlers_group_updates.on_member_left import on_member_left
from handlers_group_updates.on_admin_left import on_admin_left
from handlers_group_updates.on_member_kick import on_member_kick


router = Router()


@router.chat_member()
async def on_chat_member_update(update: ChatMemberUpdated):
    print('on_chat_member_update')

    if update.old_chat_member.status == 'left' and update.new_chat_member.status == 'member':
        return await on_member_new(update)
    elif update.old_chat_member.status == 'member' and update.new_chat_member.status == 'administrator':
        return await on_admin_new(update)
    elif update.old_chat_member.status == 'administrator' and update.new_chat_member.status == 'member':
        return on_admin_restrict_to_member(update)
    elif update.old_chat_member.status == 'administrator' and update.new_chat_member.status == 'kicked':
        return on_admin_kick(update)
    elif update.old_chat_member.status == 'member' and update.new_chat_member.status == 'left':
        return on_member_left(update)
    elif update.old_chat_member.status == 'administrator' and update.new_chat_member.status == 'left':
        return on_admin_left(update)
    elif update.old_chat_member.status == 'member' and update.new_chat_member.status == 'kicked':
        return on_member_kick(update)
    else:
        print("You haven't considered all the options")
