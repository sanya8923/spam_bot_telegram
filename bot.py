import logging
import asyncio

import config_reader

from aiogram import Bot, Dispatcher


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config_reader.config.bot_token.get_secret_value())
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

