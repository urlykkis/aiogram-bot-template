import os

from configparser import ConfigParser
from .logger import logger


class Settings:
    database_path = r"data/database.db"
    config_path = r"data/config.ini"
    logs_path = r"data/logs.log"

    config = ConfigParser()

    @classmethod
    def create_config(cls):
        cls.config.add_section("Bot")
        cls.config.set("Bot", "token", "0:0123_abc")
        cls.config.set("Bot", "admin_ids", "1046227957, ")
        cls.config.set("Bot", "logs_chat_id", "-123")
        cls.config.set("Bot", "bot_tag", "@bot_username")
        cls.config.set("Bot", "bot_username", "bot_username")
        cls.config.set("Bot", "bot_id", "0")

        with open(cls.config_path, "w") as config_file:
            cls.config.write(config_file)

    @classmethod
    def check_config_file(cls):
        if not os.path.exists(cls.config_path):
            cls.create_config()

            logger.success("Config Created.")
            exit(0)
        else:
            cls.config.read(cls.config_path)

    @classmethod
    def get_value(cls, section: str, option: str) -> str:
        value = cls.config.get(section, option)
        return value

    @classmethod
    def update_setting(cls, section: str, option: str, value: str) -> None:
        cls.config.set(section, option, value)
        with open(cls.config, "w") as config_file:
            cls.config.write(config_file)

    @classmethod
    def get_admins(cls):
        value = cls.config.get("Bot", "admin_ids")
        admin_ids = [x for x in value.split(",") if x]
        return admin_ids
