import logging
import asyncio

import config_reader

from aiogram import Bot, Dispatcher
from aiogram.types import Message

from handlers import bot_start, ban_new_user_for_links, add_stop_words, get_status_member
from handlers.get_status_member import MessageCheck, save_message_update, get_status_member, ban_new_user_for_link
from middlewares.save_message_update2 import SaveMessageUpdateMiddleware
from middlewares.stop_words import DeleteMessageForStopWords


async def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    bot = Bot(token=config_reader.config.bot_token.get_secret_value())
    dp = Dispatcher()
    # dp.message.middleware(DeleteMessageForStopWords())

    dp.include_routers(
        bot_start.router
    )


    @dp.message()
    async def message_check(message: Message):
        await save_message_update(message)
        await

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

