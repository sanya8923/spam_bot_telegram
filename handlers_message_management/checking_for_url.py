from aiogram import Router, F
from aiogram.types import Message


router = Router()


@router.message()
async def checking_for_url(message: Message) -> bool:
    entities = message.entities or []

    found_links = [
        item.extract_from(message.text) for item in entities
        if item.type == "url"
    ]

    if len(found_links) > 0:
        return True
    return False
