from aiogram import Router, F
from aiogram.types import Message
from handlers.save_message_update import members_data


router = Router()


DURATION_OF_NEW_USER_STATUS = 86400  # 24 hours


@router.message()
async def new_member_checkin(message: Message) -> Bool:

    print('get_status_member')

    date_join = [line['date_message'] for line in members_data if
                 line['user_id'] == message.from_user.id and
                 line['join_message'] is True]

    if len(date_join) > 0:
        duration_of_membership = message.date - date_join
        if duration_of_membership <= DURATION_OF_NEW_USER_STATUS:
            return True






