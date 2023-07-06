from aiogram.types import Message
from aiogram import Router

from handlers_group.on_new_message_from_new_member import on_new_message_from_new_member
from handlers_group.on_new_message_from_ordinary_member import on_new_message_from_ordinary_member

from handlers_group_management_message.check_ban_words import check_ban_words

from handlers_group_management_user.member_ban import ban_member
from handlers_group_management_user.check_new_member import check_new_member


from filter.chat_type_filter import ChatTypeFilter
from filter.user_role_filter import UserRoleFilter

from db.save_group_to_db import save_group_to_db
from db.update_users_db_from_message import update_users_db_from_message
from db.save_message_update import save_message_update


router = Router()
router.message.filter(ChatTypeFilter(chat_type=['group', 'supergroup']))


@router.message(UserRoleFilter(user_role='member'))
async def on_new_message_from_member_group(message: Message):
    print('on_new_message_from_member_group')
    await save_group_to_db(message)
    await update_users_db_from_message(message)
    await save_message_update(message)

    presence_ban_word = await check_ban_words(message)
    if presence_ban_word:
        await message.delete()
        await ban_member(message)
    else:
        new_member = await check_new_member(message)
        if new_member:
            return await on_new_message_from_new_member(message)
        else:
            return await on_new_message_from_ordinary_member(message)
