from aiogram.types import ChatMemberUpdated


async def on_kicking_bot_admin(update: ChatMemberUpdated):
    print('bot_admin_kicked')
    # TODO: TelegramBadRequest: Telegram server says Bad Request: user not found