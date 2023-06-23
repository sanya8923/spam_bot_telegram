from aiogram import Router
from aiogram.types import Message
import datetime
from lists import members_data
from constants import TIME_SPAN_TO_CHECK_NUMBER_OF_MESSAGES_MIN, ALLOWED_NUMBER_OF_MESSAGE_FOR_PERIOD

router = Router()


@router.message()
async def check_message_frequency(message: Message) -> bool:
    date_run_checking = message.date - datetime.timedelta(minutes=TIME_SPAN_TO_CHECK_NUMBER_OF_MESSAGES_MIN)
    print(f'now: {message.date}')
    print(f'date_run_checking: {date_run_checking}')

    number_of_messages_for_period = 0

    for line in members_data:
        if line.date_message > date_run_checking and line.user_id == message.from_user.id:
            number_of_messages_for_period +=1

    if number_of_messages_for_period > ALLOWED_NUMBER_OF_MESSAGE_FOR_PERIOD:
        return True
    return False


