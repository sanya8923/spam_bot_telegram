from aiogram.types import Message


async def check_for_url(message: Message) -> bool:
    entities = message.entities or []
    print('check_for_url')

    found_links = [
        item.extract_from(message.text) for item in entities
        if item.type == "url"
    ]

    if len(found_links) > 0:
        return True
    return False
