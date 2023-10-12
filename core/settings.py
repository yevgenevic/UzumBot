from dotenv import load_dotenv
from os import getenv
from dataclasses import dataclass

load_dotenv()


@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class Settings:
    bots: Bots


def get_settings():
    return Settings(
        bots=Bots(
            bot_token=getenv("TOKEN"),
            admin_id=getenv("ADMIN_ID")
        )
    )


settings = get_settings()
