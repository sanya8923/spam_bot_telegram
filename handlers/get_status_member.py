from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from handlers.save_message_update import MessageUpdate
from process_checking import check_members_data
from filter.find_link import HasLinkFilter


router = Router()


DURATION_OF_NEW_USER_STATUS = 86400  # 24 hours


class MessageCheck(StatesGroup):
    membership_term_not_defined = State()
    new_user = State()
    normal_user = State()


@router.message()
async def get_status_member(message: Message, state: FSMContext):

    await state.update_data(message_date=message.date, user_id=message.from_user.id)
    await message.answer('Hi')
    member_data = await state.get_data()
    print('get_status_member')

    date_join = [line['date_message'] for line in members_data if
                 line['user_id'] == member_data['user_id'] and
                 line['join_message'] is True]

    if len(date_join) > 0:
        duration_of_membership = member_data['message_date'] - date_join
        if duration_of_membership <= DURATION_OF_NEW_USER_STATUS:
            await state.set_state(MessageCheck.new_user)
        else:
            await state.set_state(MessageCheck.normal_user)





