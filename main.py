import logging
import asyncio

from bot import bot

from aiogram import Dispatcher
from handlers import on_new_private_message, on_new_group_supergroup_message


from middlewares.get_chat_type_middleware_outer import GetChatTypeMiddlewareOuter


async def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    dp = Dispatcher()
    dp.message.middleware(GetChatTypeMiddlewareOuter())

    dp.include_routers(
        on_new_private_message.router,
        on_new_group_supergroup_message.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

