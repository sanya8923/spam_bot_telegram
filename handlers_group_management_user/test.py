from aiogram.types import Message
from bot import bot
from handlers_group_management_user.save_group_admins import save_group_admins


async def print_chat_member(update: Message):
    # administrators = await bot.get_chat_administrators(update.chat.id)
    # for line in administrators:
    #     print(line)
    #     print(type(line))
    # print('\n')
    #
    # members = await bot.get_chat_member(update.chat.id, 6093898757)
    # for line in members:
    #     print(line)
    #     print(type(line))
    await save_group_admins(update.chat.id)

