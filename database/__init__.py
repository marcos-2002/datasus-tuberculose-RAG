from config import Config
from tortoise import Tortoise

config = Config()

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": config.DB_HOST,
                "port": 5432,
                "user": config.DB_USER,
                "password": config.DB_PASS,
                "database": config.DB_DATABASE,
            },
        },
    },
    "apps": {
        "dw": {
            "models": ["aerich.models", "database.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}

async def init():
    await Tortoise.init(config=TORTOISE_ORM)