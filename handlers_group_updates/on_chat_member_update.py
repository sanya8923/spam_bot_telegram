from aiogram import Router
from aiogram.types import ChatMemberUpdated
from handlers_group_updates.on_new_member import on_new_member
from handlers_group_updates.on_new_admin import on_new_admin


router = Router()


@router.chat_member()
async def on_chat_member_update(update: ChatMemberUpdated):

    if update.old_chat_member.status == 'left' and update.new_chat_member.status == 'member':
        return await on_new_member(update)
    elif update.old_chat_member.status == 'member' and update.new_chat_member.status == 'administrator':
        return await on_new_admin(update)
    elif update.old_chat_member.status == 'administrator' and update.new_chat_member.status == 'member':
        pass
    elif update.old_chat_member.status == 'administrator' and update.new_chat_member.status == 'kicked':
        pass
    elif update.old_chat_member.status == 'member' and update.new_chat_member.status == 'left':
        pass
    else:
        print("You haven't considered all the options")
