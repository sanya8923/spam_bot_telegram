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
        check_result = await message_manager.check()
        print(f'check_result: {check_result}')
        if check_result:
            data['violation'] = check_result
        else:
            return handler
