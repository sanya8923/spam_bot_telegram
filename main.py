import logging
import asyncio

from bot import bot

from aiogram import Dispatcher
from handlers_group import on_new_message_group_supergroup, on_update_my_chat_member
from handlers_private import on_new_message_private
from handlers_group_updates import on_update_chat_member


async def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    dp = Dispatcher()

    dp.include_routers(
        on_update_my_chat_member.router,
        on_update_chat_member.router,
        on_new_message_private.router,
        on_new_message_group_supergroup.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=['message', 'inline_query', 'chat_member', 'my_chat_member'])


if __name__ == '__main__':
    asyncio.run(main())

