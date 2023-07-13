from pydantic import BaseSettings, SecretStr


class Setting(BaseSettings):
    bot_token: SecretStr
    mongo_db: SecretStr

    class Config:
        env_file = '.env'
        env_encode = 'utf-8'


config = Setting()
