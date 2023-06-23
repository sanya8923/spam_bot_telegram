from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable
from bot import bot
from aiogram.methods.get_chat_member import GetChatMember


async def on_new_message_from_creator(message: Message):
    pass


async def on_new_message_from_admin(message: Message):
    pass


async def on_new_message_from_member(message: Message):
    pass


async def check_member_status(message: Message):
    get_chat_member = GetChatMember(
                                    chat_id=message.chat.id,
                                    user_id=message.from_user.id
                                   )
    chat_member = await bot.__call__(get_chat_member)
    if chat_member.status == 'creator':
        result = await on_new_message_from_creator(message)
    elif chat_member.status == 'administrator':
        result = await on_new_message_from_admin(message)
    elif chat_member.status == 'member':
        result = await on_new_message_from_member(message)


async def on_new_private_message(message: Message):
    pass


async def on_new_group_supergroup_message(message: Message):
    await check_member_status(message)


class GetChatTypeMiddlewareOuter(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        if event.chat.type == 'private':
            result = await on_new_private_message(event)
        elif event.chat.type == 'group':
            result = await on_new_group_supergroup_message(event)
        elif event.chat.type == 'supergroup':
            result = await on_new_group_supergroup_message(event)

        return result
