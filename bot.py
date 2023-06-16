import logging
import asyncio

import config_reader

from aiogram import Bot, Dispatcher

import processing_message
from handlers import bot_start, ban_new_user_for_links, save_message_update


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config_reader.config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_routers(
        bot_start.router,
        # save_message_update.router,
        # processing_message.router,
        ban_new_user_for_links.router,
        # save_message_update.router,
        # posting_too_often.router,
        # message_fields.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

