from pydantic import BaseSettings, SecretStr
import os

class Settings(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = os.getenv('PATH_ENV') if os.getenv('LOCATION') != 'DEV' else '.env'
        env_file_encoding = 'utf-8'

config = Settings()

