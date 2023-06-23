import logging
import asyncio

import config_reader
from bot import bot

from aiogram import Dispatcher
from handlers import save_message_update

from middlewares.get_chat_type_middleware_outer import GetChatTypeMiddlewareOuter


async def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    dp = Dispatcher()
    dp.message.middleware(GetChatTypeMiddlewareOuter())

    dp.include_routers(
        save_message_update.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

