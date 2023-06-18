import logging
import asyncio

import config_reader

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from handlers import bot_start
from handlers.get_status_member import new_member_checkin
from handlers.save_message_update import save_message_update
from handlers.ban_new_user_for_links import ban_new_user_for_link
from handlers.checking_for_url import checking_for_url


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
        user_check = await new_member_checkin(message)

        if user_check is True:
            url_presence = await checking_for_url(message)
            if url_presence is True:
                print(f'link: True')
        else:
            print(f'user_check: False')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

