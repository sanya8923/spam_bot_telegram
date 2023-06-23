import logging
import asyncio

import config_reader
from bot import bot

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

from handlers_message_check.bot_start import cmd_start
from handlers_message_check.new_member_checkin import new_member_checkin
from handlers.save_message_update import save_message_update
from handlers_user_management.ban_member import ban_member
from handlers_message_check.checking_for_url import checking_for_url
from handlers_message_check.check_message_frequency import check_message_frequency
from handlers_user_management.restrict_member import restrict_member
from handlers_message_check import add_stop_words
from handlers_user_management import unban_member

from middlewares.stop_words_checkin import DeleteMessageForStopWords
from middlewares.link_from_new_member_checkin import DeleteLinksFromNewUser

from aiogram.methods.get_chat_member import GetChatMember


async def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    dp = Dispatcher()
    # dp.message.middleware(DeleteLinksFromNewUser())

    # dp.include_routers(
    #     bot_start.router
    # )

    @dp.message()
    async def message_check(message: Message):
        if message.text == '/start':
            # await cmd_start(message)
            # await bot.get_chat_member()
            get_chat_member = GetChatMember(chat_id=message.chat.id, user_id=message.from_user.id)
            result = await bot.__call__(get_chat_member)
            print(result.json(indent=4))

        # await message.chat.unban(5430126145)
        #
        # await save_message_update(message)
        # new_member = await new_member_checkin(message)
        # url_presence = await checking_for_url(message)
        #
        # if new_member and url_presence:
        #     await message.delete()
        #     await ban_member(bot,
        #                      message,
        #                      ban_duration_min=1440)
        #
        # posting_too_often = await check_message_frequency(message,
        #                                                   duration_of_check_min=60,
        #                                                   number_of_messages=5)
        #
        # if posting_too_often:
        #     await restrict_member(bot,
        #                           message,
        #                           restrict_duration_min=10)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

