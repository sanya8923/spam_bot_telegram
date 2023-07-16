from aiogram.filters.state import StatesGroup, State


class MyState(StatesGroup):
    waiting_message_for_ban_user = State()
    waiting_message_for_unban_user = State()
