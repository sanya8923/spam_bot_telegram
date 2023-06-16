from aiogram import Router, F
from aiogram.types import Message

from filter.find_link import HasLinkFilter
from handlers.save_message_update import members_data
from middlewares.save_message_update2 import SaveMessageUpdateMiddleware

router = Router()


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



