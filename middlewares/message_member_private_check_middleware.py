from aiogram.types import Message
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from object_manager.message_manager import MessageManager


class MemberPublicMessageCheckMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       message: Message,
                       data: Dict[str, Any]) -> Any:

        print('MemberPublicMessageCheckMiddleware')
        message_manager = MessageManager(message)
        check = await message_manager.check()
        print(f'check: {check}')

        return handler
