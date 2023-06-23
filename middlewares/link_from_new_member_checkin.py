from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable

from handlers_message_check.new_member_checkin import new_member_checkin
from handlers_message_check.checking_for_url import checking_for_url
from handlers_user_management.ban_member import ban_member

from bot import bot


class DeleteLinksFromNewUser(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        new_member = await new_member_checkin(event)
        url_presence = await checking_for_url(event)

        if new_member and url_presence:
            await event.delete()
        await ban_member(bot,
                         event,
                         ban_duration_min=1440)
