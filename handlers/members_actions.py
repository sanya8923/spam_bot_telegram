from aiogram.types import Message
import datetime
import json
from constants import BAN_DURATION_MIN, RESTRICT_DURATION_MIN
from bot import bot
from db.db_mongodb import get_user_role_from_db


async def ban_member_from_group(message: Message) -> None:
    current_date = datetime.datetime.now()
    next_day = current_date + datetime.timedelta(minutes=BAN_DURATION_MIN)

    role = await get_user_role_from_db(message.from_user.id, message.chat.id)

    if bot.get_chat(message.chat.id) != 'private' and role != 'creator':
        await bot.ban_chat_member(message.chat.id,
                                  message.from_user.id,
                                  until_date=next_day,
                                  revoke_messages=False)
    else:
        pass  # TODO: добавь всплывающее окно, что админа удалить нельзя (или исключение) Посмотри как реагирует телега на удаление владельца и там реши


async def restrict_member(message: Message, *args: int) -> None:
    print('restrict_member')
    term = args[0]
    permissions = {
        "can_send_messages": False,
        "can_send_media_messages": False,
        "can_send_polls": False,
        "can_send_other_messages": False,
        "can_add_web_page_previews": False,
        "can_change_info": False,
        "can_invite_users": False,
        "can_pin_messages": False
    }

    permissions_json = json.dumps(permissions)
    current_date = datetime.datetime.now()
    if term:
        end_of_term = current_date + datetime.timedelta(minutes=term)
    else:
        end_of_term = current_date + datetime.timedelta(minutes=RESTRICT_DURATION_MIN)

    await bot.restrict_chat_member(message.chat.id,
                                   message.from_user.id,
                                   permissions=permissions_json,
                                   until_date=end_of_term)


async def unban_member(chat_id: int, user_id: int):
    print('member_unban_from_private')
    chat = await bot.get_chat(chat_id)
    await chat.unban(user_id, only_if_banned=False)


async def restrict_admin_to_member(chat_id: int, user_id: int):
    print('restrict_admin_to_member')
    new_role = await bot.promote_chat_member(chat_id,
                                             user_id,
                                             can_change_info=False,
                                             can_post_messages=False,
                                             can_edit_messages=False,
                                             can_delete_messages=False,
                                             can_invite_users=False,
                                             can_restrict_members=False,
                                             can_pin_messages=False,
                                             can_promote_members=False)
    print(f'new_role: {new_role}')
    # TODO: after promote all don't work





