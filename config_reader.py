from pydantic import BaseSettings, SecretStr, validator
import os

class Settings(BaseSettings):
    # Желательно вместо str использовать SecretStr 
    # для конфиденциальных данных, например, токена бота
    bot_token: SecretStr

    # Вложенный класс с дополнительными указаниями для настроек
    class Config:
        # Имя файла, откуда будут прочитаны данные 
        # (относительно текущей рабочей директории)
        env_file = '.env'
        # Кодировка читаемого файла
        env_file_encoding = 'utf-8'

    # Define a validator function for the bot_token field
    @validator("bot_token", pre=True)
    def get_bot_token(cls, value):
        # If the value is not provided, try to get it from the environment variable BOT_TOKEN
        if value is None:
            value = os.environ.get("BOT_TOKEN")
        # Return the value or raise an exception if it is still None
        if value is None:
            raise ValueError("No bot token provided")
        return value

# При импорте файла сразу создастся 
# и провалидируется объект конфига, 
# который можно далее импортировать из разных мест
config = Settings()
