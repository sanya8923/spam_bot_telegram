from aiogram import BaseMiddleware, F
from aiogram.types import Message
from aiogram.methods.delete_message import DeleteMessage
from typing import Callable, Dict, Any, Awaitable
from handlers_management_message.add_stop_words import stop_words


class DeleteMessageForStopWords(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        if F.text == 'гашиш':
            return DeleteMessage(chat_id=event.chat.id, message_id=event.message_id)
        else:
            return await handler(event, data)
