from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from handlers.save_message_update import MessageUpdate
from check_process import check_members_data


router = Router()


class MessageCheck(StatesGroup):
    membership_term_not_defined = State()
    new_user = State()
    normal_user = State()


members_data = []


@router.message()
async def save_message_update(message: Message, state: FSMContext) -> None:
    await state.set_state(MessageCheck.membership_term_not_defined)

    item = MessageUpdate()
    item.user_id = message.from_user.id
    item.chat_id = message.chat.id
    item.message_id = message.message_id
    item.date_message = message.date

    data_join = message.new_chat_members
    if data_join is not None:
        item.join_message = True

    members_data.append(item)
    check_members_data(members_data)



