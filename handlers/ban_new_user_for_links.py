from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from filter.find_link import HasLinkFilter


router = Router()


@router.message(F.text, HasLinkFilter())
async def ban_new_user_for_link(message: Message, links: list[str]):
    await message.reply(f"Thanks for link {', '.join(links)}")
