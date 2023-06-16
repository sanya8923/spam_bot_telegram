from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Optional, Callable, Dict, Any, Awaitable
import datetime


members_data = []


class MessageUpdate:
    user_id: int
    chat_id: int
    message_id: int
    date_message: datetime
    join_message: Optional[bool] = False


class SaveMessageUpdateMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        item = MessageUpdate()
        item.user_id = event.from_user.id
        item.chat_id = event.chat.id
        item.message_id = event.message_id
        item.date_message = event.date

        data_join = event.new_chat_members
        if data_join is not None:
            item.join_message = True

        members_data.append(item)
        for line in members_data:
            print(f'user_id: {line.user_id}'
                  f'\nchat_id: {line.chat_id}'
                  f'\nmessage_id: {line.message_id}'
                  f'\ndate_message: {line.date_message}')

        return await handler(event, data)



