from aiogram.types import Message
from db.db_mongodb import db
import datetime
from datetime import timedelta
from constants import TIME_SPAN_TO_CHECK_NUMBER_OF_MESSAGES_MIN, ALLOWED_NUMBER_OF_MESSAGE_FOR_PERIOD, \
    DURATION_OF_NEW_USER_STATUS
from handlers.member_ban import ban_member
from handlers.member_restrict import restrict_member


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


async def check_membership_groups(user_id: int):
    print('check_membership_groups')

    collection_group_user_role = db['group_user_role']
    documents_group_user_role = collection_group_user_role.find({'user_id': user_id})

    chat_id_list = []
    async for document in documents_group_user_role:
        chat_id_list.append(document['chat_id'])

    collection_groups = db['groups']
    chat_data = []

    for chat_id in set(chat_id_list):
        documents_groups = collection_groups.find({f'chat_id': chat_id})
        async for document in documents_groups:
            chat_data.append((document['chat_name'], document['chat_username'], document['chat_id']))

    return chat_data


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


async def check_message_frequency(message: Message) -> bool:
    time_span_to_check = datetime.timedelta(minutes=TIME_SPAN_TO_CHECK_NUMBER_OF_MESSAGES_MIN)
    date_run_checking = message.date - time_span_to_check

    number_of_messages_for_period = 1

    collection = db[f'{message.chat.id} - message updates']

    async for _ in collection.find(
            {'date_message': {'$gt': date_run_checking}, 'user_id': message.from_user.id}):
        number_of_messages_for_period += 1

    if number_of_messages_for_period >= ALLOWED_NUMBER_OF_MESSAGE_FOR_PERIOD:
        return True
    return False


async def check_message_from_new_member(message: Message):
    presence_url = await check_for_url(message)
    if presence_url:
        await message.delete()
        await ban_member(message)
    else:
        posting_too_often = await check_message_frequency(message)
        if posting_too_often:
            await restrict_member(message)


async def check_message_from_ordinary_member(message: Message):
    print('on_new_message_from_ordinary_member')
    posting_too_often = await check_message_frequency(message)
    if posting_too_often:
        await restrict_member(message)


async def check_new_member(message: Message) -> bool:
    new_member_pattern = message.date - timedelta(seconds=DURATION_OF_NEW_USER_STATUS)

    collection = db[f'{message.chat.id} - message updates']
    async for doc in collection.find(
            {'date_message': {'$gt': new_member_pattern}, 'user_id': message.from_user.id}):
        if doc.get('join_message'):
            return True
        else:
            return False
