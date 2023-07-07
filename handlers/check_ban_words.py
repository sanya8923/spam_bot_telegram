from aiogram.types import Message
from db.db_mongodb import db


async def check_ban_words(message: Message) -> bool:
    collection = db['ban_words']
    banned_words = (await collection.find_one())['words']

    if message.text is None:
        return False

    words_in_message = message.text.lower().split()

    for banned_word in banned_words:
        if banned_word in words_in_message:
            return True
    return False



