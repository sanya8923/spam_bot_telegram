from aiogram import Router
from aiogram.types import Message
from typing import Coroutine

from handlers_group_management_user.get_member_status_group_supergroup import get_member_status_group_supergroup

from handlers_group.on_new_message_from_creator import on_new_message_from_creator
from handlers_group.on_new_message_from_admin import on_new_message_from_admin
from handlers_group.on_new_message_from_member import on_new_message_from_member
from handlers_group_management_user.save_user import save_user
from handlers_group_management_message.save_message_update import save_message_update
from handlers_group.save_group import save_group


router = Router()


@router.message()
async def on_new_group_supergroup_message(message: Message) -> Coroutine:
    await save_group(message)
    await save_user(message)
    await save_message_update(message)

    chat_member_status = await get_member_status_group_supergroup(message)
    if chat_member_status == 'creator':
        return await on_new_message_from_creator(message)
    elif chat_member_status == 'administrator':
        return await on_new_message_from_admin(message)
    elif chat_member_status == 'member':
        return await on_new_message_from_member(message)

