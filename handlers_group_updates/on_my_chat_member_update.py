from aiogram import Router, F
from aiogram.types import Update
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, MEMBER, ADMINISTRATOR, KICKED, JOIN_TRANSITION
from aiogram.types import ChatMemberUpdated
from handlers_group_updates.on_adding_bot_to_group_by_member import on_adding_bot_to_group_by_member
from handlers_group_updates.on_adding_bot_to_group_by_admin import on_adding_bot_to_group_by_admin
from handlers_group_updates.on_demote_bot_from_admin_to_member import on_demote_bot_from_admin_to_member
from handlers_group_updates.on_kicking_bot_admin import on_kicking_bot_admin
from handlers_group_updates.on_left_bot_member_from_group import on_left_bot_member_from_group

router = Router()
# router.my_chat_member.filter(F.chat.type == 'group' or F.chat.type == 'supergroup')
# router.message.filter(F.chat.type == 'group' or F.chat.type == 'supergroup')


@router.my_chat_member()
async def on_my_chat_member_update(update: ChatMemberUpdated):

    if update.old_chat_member.status == 'left' and update.new_chat_member.status == 'member':
        return await on_adding_bot_to_group_by_member(update)
    elif update.old_chat_member.status == 'member' and update.new_chat_member.status == 'administrator':
        return await on_adding_bot_to_group_by_admin(update)
    elif update.old_chat_member.status == 'administrator' and update.new_chat_member.status == 'member':
        return await on_demote_bot_from_admin_to_member(update)
    elif update.old_chat_member.status == 'administrator' and update.new_chat_member.status == 'kicked':
        return await on_kicking_bot_admin(update)
    elif update.old_chat_member.status == 'member' and update.new_chat_member.status == 'left':
        return await on_left_bot_member_from_group(update)
    else:
        print("You haven't considered all the options")
