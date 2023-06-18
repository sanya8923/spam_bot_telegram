import logging
import asyncio

import config_reader

from aiogram import Bot, Dispatcher
from aiogram.types import Message

from handlers import bot_start
from handlers.get_status_member import new_member_checkin
from handlers.save_message_update import save_message_update


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
        await new_member_checkin(message)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

