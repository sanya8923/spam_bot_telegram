from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from handlers.save_message_update import MessageUpdate, members_data


router = Router()


class MessageCheck(StatesGroup):
    state = State()





