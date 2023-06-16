from aiogram import Router

from handlers.save_message_update import MessageUpdate


router = Router()


class MessageProcessor:
    def __init__(self, bot):
        self.bot = bot
        self.message_data = MessageUpdate()

    async def delete_message(self, chat_id: int, message_id: int):
        await self.bot.delete_message(chat_id=chat_id, message_id=message_id)

