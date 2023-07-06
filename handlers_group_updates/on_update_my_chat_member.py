from aiogram import Router
from aiogram.types import ChatMemberUpdated
from handlers_group_updates.on_add_bot_by_member import on_add_bot_by_member
from handlers_group_updates.on_bot_add_by_admin import on_bot_add_by_admin
from handlers_group_updates.on_bot_admin_to_member_restrict import on_bot_admin_to_member_restrict
from handlers_group_updates.on_bot_admin_kick import on_bot_admin_kick
from handlers_group_updates.on_bot_member_left import on_bot_member_left
from filter.chat_type_filter import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(chat_type=['group', 'supergroup']))


@router.my_chat_member()
async def on_my_chat_member_update(update: ChatMemberUpdated):
    print('on_my_chat_member_update')
    if update.old_chat_member.status == 'left' and update.new_chat_member.status == 'member':
        print('on_add_bot_by_member')
        return await on_add_bot_by_member(update)
    elif update.old_chat_member.status == 'member' and update.new_chat_member.status == 'administrator':
        print('on_bot_add_by_admin')
        return await on_bot_add_by_admin(update)
    elif update.old_chat_member.status == 'administrator' and update.new_chat_member.status == 'member':
        return await on_bot_admin_to_member_restrict(update)
    elif update.old_chat_member.status == 'administrator' and update.new_chat_member.status == 'kicked':
        return await on_bot_admin_kick(update)
    elif update.old_chat_member.status == 'member' and update.new_chat_member.status == 'left':
        return await on_bot_member_left(update)
    else:
        print("You haven't considered all the options")
