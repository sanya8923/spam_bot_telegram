from aiogram.filters.state import StatesGroup, State


class MyState(StatesGroup):
    waiting_message = State()
