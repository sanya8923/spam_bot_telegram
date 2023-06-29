from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable

from handlers_group.on_new_group_supergroup_message import on_new_group_supergroup_message
from handlers_group.on_new_private_message import on_new_private_message


class GetChatTypeMiddlewareOuter(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ):
        if event.chat.type == 'private':
            return await on_new_private_message(event)
        elif event.chat.type == 'group':
            return await on_new_group_supergroup_message(event)
        elif event.chat.type == 'supergroup':
            return await on_new_group_supergroup_message(event)

