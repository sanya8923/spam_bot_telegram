from aiogram import Router, F
from aiogram.types import Update
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, MEMBER, ADMINISTRATOR, KICKED, JOIN_TRANSITION
from aiogram.types import ChatMemberUpdated

router = Router()
# router.my_chat_member.filter(F.chat.type == 'group' or F.chat.type == 'supergroup')
# router.message.filter(F.chat.type == 'group' or F.chat.type == 'supergroup')


@router.my_chat_member()
async def get_chat_id_from_new_group(update: ChatMemberUpdated) -> int:
    print(update.json(indent=4))
    return update.chat.id

