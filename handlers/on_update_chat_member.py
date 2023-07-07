from aiogram import Router
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, ChatMemberUpdated, JOIN_TRANSITION, \
    PROMOTED_TRANSITION, IS_ADMIN, MEMBER, IS_MEMBER, LEFT, KICKED
from filter.chat_type_filter import ChatTypeFilter
from db.update_users_db_from_member_update import update_users_db_from_member_update
from db.update_group_user_role_db import update_group_user_role_db


router = Router()
router.message.filter(ChatTypeFilter(chat_type=['group', 'supergroup']))


@router.chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def on_new_member(update: ChatMemberUpdated):
    print('on_new_member')
    await update_users_db_from_member_update(update)
    await update_group_user_role_db(update)


@router.chat_member(ChatMemberUpdatedFilter(member_status_changed=PROMOTED_TRANSITION))
async def on_admin_new(update: ChatMemberUpdated):
    print('on_new_admin')
    await update_group_user_role_db(update)


@router.chat_member(ChatMemberUpdatedFilter(IS_ADMIN >> MEMBER))
async def on_admin_downgrade_to_member(update: ChatMemberUpdated):
    print('on_admin_downgrade_to_member')
    await update_group_user_role_db(update)


@router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> LEFT))
async def on_admin_member_left(update: ChatMemberUpdated):
    print('on_admin_member_left')
    await update_group_user_role_db(update)


@router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> KICKED))
async def on_admin_member_kick(update: ChatMemberUpdated):
    print('on_admin_member_kick')
    await update_group_user_role_db(update)

