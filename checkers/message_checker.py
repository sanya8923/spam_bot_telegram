from aiogram.types import Message
from datetime import timedelta
from constants import DURATION_OF_NEW_USER_STATUS
from db.db_mongodb import db


class MessageChecker:
    def __init__(self, message: Message):
        self.message = message
        self.member = self.message.from_user
        self.group = self.message.chat

    async def check_new_member(self) -> bool:
        print('check_new_member')
        new_member_pattern = self.message.date - timedelta(seconds=DURATION_OF_NEW_USER_STATUS)

        collection = db[f'{self.group.id} - messages']
        async for doc in collection.find(
                {'date_message': {'$gt': new_member_pattern}, 'user_id': self.member.id}):
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
        collection = db['ban_words']
        banned_words = (await collection.find_one())['words']

        if self.message.text is None:
            return False

        words_in_message = self.message.text.lower().split()

        for banned_word in banned_words:
            if banned_word in words_in_message:
                return True
        return False

