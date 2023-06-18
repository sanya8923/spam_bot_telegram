from aiogram import Router, F
from aiogram.types import Message

from filter.find_link import HasLinkFilter
from handlers.save_message_update import members_data
from middlewares.save_message_update2 import SaveMessageUpdateMiddleware

router = Router()


# @router.message(F.text, HasLinkFilter())
# async def ban_new_user_for_link(message: Message, links: list[str]):
#     print(f'links: {links}')
    # if links:
    #     await message.reply(f"Thanks for link {links}")
    # else:
    #     await message.reply(f"Message list {members_data}")


@router.message()
async def ban_new_user_for_link(message: Message):
    entities = message.entities or []

    found_links = [
        item.extract_from(message.text) for item in entities
        if item.type == "url"
    ]

    print(f'found_links: {found_links}')

    if len(found_links) > 0:
        print('link_founded')



