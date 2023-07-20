from aiogram.types import Message
from aiogram import Router

from filter.chat_type_filter import ChatTypeFilter
from filter.user_role_filter import UserRoleFilter

from db.update_users_db_from_message import update_users_db_from_message
from db.save_message_update import save_message_update
from db.update_group_user_role_db import update_group_user_role_db
from db.db_mongodb import update_role_to_db

from handlers.members_actions import ban_member_from_group
from handlers.checks_handlers import check_message_from_new_member, check_message_from_ordinary_member, check_ban_words, \
    check_new_member


router = Router()
router.message.filter(ChatTypeFilter(chat_type=['group', 'supergroup']))


@router.message(UserRoleFilter(user_role='creator'))
async def on_new_message_from_creator_group(message: Message):
    print('on_new_message_from_creator_group')

    await update_users_db_from_message(message)
    await save_message_update(message)


@router.message(UserRoleFilter(user_role='administrator'))
async def on_new_message_from_admin_group(message: Message):
    print('on_new_message_from_admin_group')

    await update_users_db_from_message(message)
    await save_message_update(message)


@router.message(UserRoleFilter(user_role='member'))
async def on_new_message_from_member_group(message: Message):
    print('on_new_message_from_member_group')

    await update_users_db_from_message(message)
    await update_role_to_db(message.chat.id, message=message)
    await save_message_update(message)

    presence_ban_word = await check_ban_words(message)
    if presence_ban_word:
        await message.delete()
        await ban_member_from_group(message)
    else:
        new_member = await check_new_member(message)
        if new_member:
            await check_message_from_new_member(message)
        return await check_message_from_ordinary_member(message)


