from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable
from bot import bot
from aiogram.methods.get_chat_member import GetChatMember
from handlers_user_management.ban_member import ban_member
from handlers_user_management.restrict_member import restrict_member
from handlers_message_check.new_member_checkin import new_member_checkin
from handlers_message_check.checking_for_url import checking_for_url
from handlers_message_check.check_message_frequency import check_message_frequency
from handlers.save_message_update import save_message_update


async def on_new_message_from_new_member(message: Message):
    presence_url = await checking_for_url(message)
    if presence_url:
        await message.delete()
        await ban_member(message)
    else:
        posting_too_often = await check_message_frequency(message)
        if posting_too_often:
            await restrict_member(message)
        else:
            await save_message_update(message)


async def on_new_message_from_ordinary_member(message: Message):
    posting_too_often = await check_message_frequency(message)
    if posting_too_often:
        await restrict_member(message)
    else:
        await save_message_update(message)


async def check_ban_words(message: Message) -> bool:
    pass


async def on_new_message_from_creator(message: Message):
    pass


async def on_new_message_from_admin(message: Message):
    pass


async def on_new_message_from_member(message: Message):
    # check ban_words
    presence_ban_word = await check_ban_words(message)
    if presence_ban_word:
        await message.delete()
        await ban_member(message)
    else:
    # check duration membership
        new_member = await new_member_checkin(message)
        if new_member:
            result = await on_new_message_from_new_member(message)
        else:
            result = await on_new_message_from_ordinary_member(message)
    return result




async def check_member_status(message: Message):
    get_chat_member = GetChatMember(
                                    chat_id=message.chat.id,
                                    user_id=message.from_user.id
                                   )
    chat_member = await bot.__call__(get_chat_member)
    if chat_member.status == 'creator':
        result = await on_new_message_from_creator(message)
    elif chat_member.status == 'administrator':
        result = await on_new_message_from_admin(message)
    elif chat_member.status == 'member':
        result = await on_new_message_from_member(message)


async def on_new_private_message(message: Message):
    pass


async def on_new_group_supergroup_message(message: Message):
    await check_member_status(message)


class GetChatTypeMiddlewareOuter(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        if event.chat.type == 'private':
            result = await on_new_private_message(event)
        elif event.chat.type == 'group':
            result = await on_new_group_supergroup_message(event)
        elif event.chat.type == 'supergroup':
            result = await on_new_group_supergroup_message(event)

        return result
