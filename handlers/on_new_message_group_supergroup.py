from aiogram.types import Message
from aiogram import Router

from filter.chat_type_filter import ChatTypeFilter
from filter.user_role_filter import UserRoleFilter

from db.update_users_db_from_message import update_users_db_from_message
from db.save_message_update import save_message_update
from db.db_mongodb import update_role_to_db

from handlers.members_actions import ban_member_from_group
from handlers.checks_handlers import check_message_from_new_member, check_message_from_ordinary_member, check_ban_words, \
    check_new_member

from db_manager.db_manager import DbManager
from data_manager.data_manager import DataManager


router = Router()
router.message.filter(ChatTypeFilter(chat_type=['group', 'supergroup']))


@router.message(UserRoleFilter(user_role='creator'))
async def on_new_message_from_creator_group(message: Message):
    print('on_new_message_from_creator_group')
    data_manager = DataManager()
    message_object = await data_manager.save_message(message)  # types: MessageData
    check_save_to_db = await data_manager.save_to_db(message_object)  # types: bool



@router.message(UserRoleFilter(user_role='administrator'))
async def on_new_message_from_admin_group(message: Message):
    print('on_new_message_from_admin_group')

    data_manager = DataManager()
    message_object = await data_manager.save_message(message)  # types: MessageData
    check_save_to_db = await data_manager.save_to_db(message_object)  # types: bool


@router.message(UserRoleFilter(user_role='member'))
async def on_new_message_from_member_group(message: Message):
    print('on_new_message_from_member_group')
    data_manager = DataManager()
    message_objects = await data_manager.save_message(message)  # types: MessageData
    check_save_to_db = await data_manager.save_to_db(message_objects)  # types: bool
    check_message = await data_manager.check_message(message_objects)  # types: bool

    # await update_users_db_from_message(message)
    # await update_role_to_db(message.chat.id, message=message)
    # await save_message_update(message)
    #
    # presence_ban_word = await check_ban_words(message)
    # if presence_ban_word:
    #     await message.delete()
    #     await ban_member_from_group(message)
    # else:
    #     new_member = await check_new_member(message)
    #     if new_member:
    #         await check_message_from_new_member(message)
    #     else:
    #         await check_message_from_ordinary_member(message)


