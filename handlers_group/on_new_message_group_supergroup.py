from aiogram import Router
from aiogram.types import Message
from typing import Coroutine

from handlers_group_management_user.get_member_status_group_supergroup import get_member_status_group_supergroup

from handlers_group.on_new_message_from_creator import on_new_message_from_creator
from handlers_group.on_new_message_from_admin import on_new_message_from_admin
from handlers_group.on_new_message_from_member import on_new_message_from_member
from handlers_group_management_user.update_users_db_from_message import update_users_db_from_message
from handlers_group_management_message.save_message_update import save_message_update
from handlers_group.save_group import save_group


router = Router()


@router.message()
async def on_new_message_group_supergroup(message: Message) -> Coroutine:
    await save_group(message)
    await update_users_db_from_message(message)
    await save_message_update(message)

    chat_member_status = await get_member_status_group_supergroup(message)
    if chat_member_status == 'creator':
        return await on_new_message_from_creator(message)
    elif chat_member_status == 'administrator':
        return await on_new_message_from_admin(message)
    elif chat_member_status == 'member':
        return await on_new_message_from_member(message)

