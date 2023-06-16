from aiogram import Router, F
from aiogram.types import Message

from filter.find_link import HasLinkFilter
from handlers.save_message_update2 import members_data

router = Router()


@router.message(F.text, HasLinkFilter())
async def ban_new_user_for_link(message: Message, links: list[str]):

    if links:
        await message.reply(f"Thanks for link {', '.join(links)}"
                            f"Message list {members_data}")
    else:
        await message.reply(f"Message list {members_data}")



