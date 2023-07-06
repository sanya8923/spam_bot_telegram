from aiogram.types import Message
from aiogram import Router

from filter.chat_type_filter import ChatTypeFilter
from filter.user_role_filter import UserRoleFilter

from db.save_group_to_db import save_group_to_db
from db.update_users_db_from_message import update_users_db_from_message
from db.save_message_update import save_message_update


router = Router()
router.message.filter(ChatTypeFilter(chat_type=['group', 'supergroup']))


@router.message(UserRoleFilter(user_role='administrator'))
async def on_new_message_from_admin_group(message: Message):
    print('on_new_message_from_admin_group')
    await save_group_to_db(message)
    await update_users_db_from_message(message)
    await save_message_update(message)
