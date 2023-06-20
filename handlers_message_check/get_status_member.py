from aiogram import Router, F
from aiogram.types import Message
from handlers.save_message_update import members_data
import datetime


router = Router()


DURATION_OF_NEW_USER_STATUS = 86400  # 24 hours


@router.message()
async def new_member_checkin(message: Message) -> bool:

    date_join = None
    user_id = None
    for line in members_data:
        if line.join_message is True:
            date_join = line.date_message
            user_id = line.user_id

    if date_join is not None:
        duration_of_membership = message.date - date_join
        if (message.from_user.id == user_id) and \
                (duration_of_membership.total_seconds() <= DURATION_OF_NEW_USER_STATUS):
            return True
        else:
            return False


