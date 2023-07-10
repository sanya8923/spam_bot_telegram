from aiogram import Router
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, JOIN_TRANSITION, PROMOTED_TRANSITION, \
    LEAVE_TRANSITION, IS_ADMIN, MEMBER
from aiogram.types import ChatMemberUpdated

from db.save_admins_to_db import save_admins_to_db
from db.save_group_to_db import save_group_to_db

from filter.chat_type_filter import ChatTypeFilter

from db.delete_chat_id_from_groups_db import delete_chat_id_from_groups_db

from aiogram.exceptions import TelegramForbiddenError
from contextlib import suppress


router = Router()
router.message.filter(ChatTypeFilter(chat_type=['group', 'supergroup']))


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def on_add_bot_by_member(update: ChatMemberUpdated):
    print('bot added to group - member')
    await save_group_to_db(update)


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=PROMOTED_TRANSITION))
async def on_add_bot_by_admin(update: ChatMemberUpdated):
    print('bot added to group - admin')

    await save_admins_to_db(update)



@router.my_chat_member(ChatMemberUpdatedFilter(IS_ADMIN >> MEMBER))
async def on_downgrade_bot(update: ChatMemberUpdated):
    print('bot downgrade from admin to member')


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=LEAVE_TRANSITION))
async def on_leave_bot_from_group(update: ChatMemberUpdated):
    with suppress(TelegramForbiddenError):
        print('bot leave the group')
        await delete_chat_id_from_groups_db(update)



