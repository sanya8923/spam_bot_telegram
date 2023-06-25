from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable

from handlers_management_user.check_new_member import check_new_member
from handlers_management_message.check_message_for_url import check_for_url
from handlers_management_user.member_ban import ban_member

from bot import bot


class DeleteLinksFromNewUser(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        new_member = await check_new_member(event)
        url_presence = await check_for_url(event)

        if new_member and url_presence:
            await event.delete()
        await ban_member(bot,
                         event,
                         ban_duration_min=1440)
