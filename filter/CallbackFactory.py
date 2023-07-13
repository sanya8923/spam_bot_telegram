from aiogram.filters.callback_data import CallbackData


class CallbackFactory(CallbackData, prefix='data'):
    type: str
    chat_id: int
    chat_username: str
    chat_name: str
    user_id: int
    username: str
    first_name: str
    last_name: str

