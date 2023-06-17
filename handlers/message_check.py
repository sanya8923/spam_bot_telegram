from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from handlers.save_message_update import MessageUpdate
from check_process import check_members_data
from filter.find_link import HasLinkFilter



router = Router()


DURATION_OF_NEW_USER_STATUS = 86400


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


@router.message()
async def get_status_member(message: Message, state: FSMContext):
    date_join = [line['date_message'] for line in members_data if
                 line['user_id'] == message.from_user.id and
                 line['join_message'] is True]

    if len(date_join) > 0:
        duration_of_membership = message.date - date_join

        if duration_of_membership <= DURATION_OF_NEW_USER_STATUS:
            await state.set_state(MessageCheck.new_user)
        else:
            await state.set_state(MessageCheck.normal_user)


@router.message(F.text, HasLinkFilter())
async def ban_new_user_for_link(message: Message, links: list[str]):
    print("IT'S HANDLER")
    for line in members_data:
        print(f'user_id: {line.user_id}'
              f'\nchat_id: {line.chat_id}'
              f'\nmessage_id: {line.message_id}'
              f'\ndate_message: {line.date_message}')
    if links:
        await message.reply(f"Thanks for link {', '.join(links)}"
                            f"Message list {members_data}")
    else:
        await message.reply(f"Message list {members_data}")



