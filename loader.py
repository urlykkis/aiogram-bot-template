from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from utils import Settings


Settings.check_config_file()


storage = MemoryStorage()
bot = Bot(Settings.get_value("Bot", "token"), parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler()
