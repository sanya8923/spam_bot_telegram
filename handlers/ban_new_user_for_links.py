from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from filter.find_link import HasLinkFilter
from handlers.save_message_update import MessageUpdate


router = Router()


@router.message(F.text, HasLinkFilter(), MessageUpdate())
async def ban_new_user_for_link(message: Message, links: list[str], message_list: list[MessageUpdate]):
    if links:
        await message.reply(f"Thanks for link {', '.join(links)}"
                            f"Message list {message_list}")
    else:
        await message.reply(f"Message list {message_list}")



