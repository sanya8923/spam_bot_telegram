import datetime
import logging
import asyncio

import config_reader

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from handlers import bot_start
from handlers.get_status_member import new_member_checkin
from handlers.save_message_update import save_message_update
from handlers.ban_member import ban_member
from handlers.checking_for_url import checking_for_url
from handlers.check_message_frequency import check_message_frequency


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
        new_member = await new_member_checkin(message)
        url_presence = await checking_for_url(message)

        if new_member and url_presence:
            await message.delete()
            await ban_member(bot, message, ban_duration=1)

        await check_message_frequency(message, duration_of_check_min=60, number_of_messages=10)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

