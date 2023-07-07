from aiogram import Router, F
from aiogram.types import Message
from filter.chat_type_filter import ChatTypeFilter


router = Router()
router.message.filter(ChatTypeFilter(chat_type='private'))


@router.message(F.text.contains('('))
async def management_group(message: Message):

