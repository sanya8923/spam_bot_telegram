from aiogram.types import Message
from datetime import timedelta
from constants import DURATION_OF_NEW_USER_STATUS
from aiogram import Dispatcher



class MessageChecker:
    def __init__(self, message: Message):
        self.message = message

    async def check_new_member(self) -> bool:
        new_member_pattern = self.message.date - timedelta(seconds=DURATION_OF_NEW_USER_STATUS)

        collection = db[f'{self.message.chat.id} - message updates']
        async for doc in collection.find(
                {'date_message': {'$gt': new_member_pattern}, 'user_id': self.message.from_user.id}):
            if doc.get('join_message'):
                return True
            else:
                return False

    async def url_check(self) -> bool:
        print(f'url_check')
        entities = self.message.entities or []
        print('check_for_url')

        found_links = [
            item.extract_from(self.message.text) for item in entities
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

