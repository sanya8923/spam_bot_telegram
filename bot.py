from aiogram import Bot
import config_reader

bot = Bot(token=config_reader.config.bot_token.get_secret_value())
