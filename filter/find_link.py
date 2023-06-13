from typing import Union, Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message


class HasLinkFilter(BaseFilter):
    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        entities = message.entities or []

        found_links = [
            item.extract_from(message.text) for item in entities
            if item.type == "url"
        ]
        print(f'found_links: {found_links}')

        if len(found_links) > 0:
            return {"links": found_links}
        return False
