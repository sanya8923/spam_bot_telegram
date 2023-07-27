from aiogram.types import Message


class MessageChecker:
    def __init__(self, message: Message):
        self.message = message

    async def url_check(self) -> bool:
        print(f'url_check')
        entities = message.entities or []
        print('check_for_url')

        found_links = [
            item.extract_from(message.text) for item in entities
            if item.type == "url"
        ]

        if len(found_links) > 0:
            return True
        return False

    async def flood_check(self) -> bool:
        print(f'flood_check')
        return True

    async def ban_words_check(self) -> bool:
        print('ban_words_check')
        return True

