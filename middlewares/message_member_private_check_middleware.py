from aiogram.types import TelegramObject, Message
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any


class MemberPublicMessageCheckMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]) -> Any:

        pass
