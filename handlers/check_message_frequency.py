from aiogram import Router
from aiogram.types import Message
import datetime
from handlers.save_message_update import members_data


router = Router()


@router.message()
async def check_message_frequency(message: Message, duration_of_check_min: int, number_of_messages: int) -> bool:
    date_run_checking = message.date - datetime.timedelta(minutes=duration_of_check_min)
    print(f'now: {message.date}')
    print(f'date_run_checking: {date_run_checking}')

    number_of_messages_for_period = 0

    for line in members_data:
        if line.date_message > date_run_checking and line.user_id == message.from_user.id:
            number_of_messages_for_period +=1

    if number_of_messages_for_period > number_of_messages:
        return True
    return False


