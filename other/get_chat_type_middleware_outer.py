from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable

from handlers.on_new_message_group_supergroup import on_new_message_group_supergroup
# from handlers.on_new_message_private import on_new_message_private


class GetChatTypeMiddlewareOuter(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ):
        if event.chat.type == 'private':
            return await on_new_message_private(event)
        elif event.chat.type == 'group':
            return await on_new_message_group_supergroup(event)
        elif event.chat.type == 'supergroup':
            return await on_new_message_group_supergroup(event)

