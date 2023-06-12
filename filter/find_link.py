from aiogram.types import Message
from aiogram.filters import BaseFilter


class HasLinkFilter(BaseFilter):
    async def __call__(self, message: Message):
        entities = message.entities or []

        found_link = [
            item.extract_from(message.text) for item in message.entities
            if item.url is not None
        ]

        if len(found_link) > 0:
            return {'find link': found_link}
        return False
