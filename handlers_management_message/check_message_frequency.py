from aiogram.types import Message
import datetime
from constants import TIME_SPAN_TO_CHECK_NUMBER_OF_MESSAGES_MIN, ALLOWED_NUMBER_OF_MESSAGE_FOR_PERIOD
from db.db_mongodb import db


async def check_message_frequency(message: Message) -> bool:
    time_span_to_check = datetime.timedelta(minutes=TIME_SPAN_TO_CHECK_NUMBER_OF_MESSAGES_MIN)
    date_run_checking = message.date - time_span_to_check
    print('check_message_frequency')

    number_of_messages_for_period = 1

    collection = db[str(message.chat.id)]
    async for _ in collection.find(
            {"date_message": {"$gt": date_run_checking}, "user_id": message.from_user.id}):
        number_of_messages_for_period += 1
        print(f'count: {number_of_messages_for_period}')

    if number_of_messages_for_period >= ALLOWED_NUMBER_OF_MESSAGE_FOR_PERIOD:
        return True
    return False


