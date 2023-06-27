from aiogram import Router
from aiogram.types import Message
from typing import Coroutine

from handlers_management_user.get_member_status_group_supergroup import get_member_status_group_supergroup

from handlers.on_new_message_from_creator import on_new_message_from_creator
from handlers.on_new_message_from_admin import on_new_message_from_admin
from handlers.on_new_message_from_member import on_new_message_from_member
from handlers_management_user.member_unban import member_unban


router = Router()


@router.message()
async def on_new_group_supergroup_message(message: Message) -> Coroutine:
    chat_member_status = await get_member_status_group_supergroup(message)
    if chat_member_status == 'creator':
        print('creator')
        return await on_new_message_from_creator(message)
    elif chat_member_status == 'administrator':
        return await on_new_message_from_admin(message)
    elif chat_member_status == 'member':
        return await on_new_message_from_member(message)

