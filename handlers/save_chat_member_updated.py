from aiogram.types import ChatMemberUpdated
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, IS_MEMBER, IS_NOT_MEMBER
from aiogram import Router
from aiogram.types.chat_join_request import ChatJoinRequest


router = Router()


# @router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
@router.chat_member()
async def on_chat_member_update(event: ChatMemberUpdated):
    print(f'new member: {event.from_user.id}')

@router.chat_join_request()
async def on_chat_join_request(event: ChatJoinRequest):
    print(f'chat join request', event)


# @router.chat_member(ChatMemberUpdatedFilter())