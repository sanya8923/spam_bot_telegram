from aiogram.types import TelegramObject, Message
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from object_manager.message_manager import MessageManager


class MemberPublicMessageCheckMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]) -> Any:

        print('MemberPublicMessageCheckMiddleware')
        message_manager = MessageManager(event)

        return handler
