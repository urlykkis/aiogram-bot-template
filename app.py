from aiogram import Dispatcher, executor

from handlers import dp
from loader import scheduler
from utils import set_commands, create_tables, setup_logger
from middleware import ThrottlingMiddleware


async def on_startup(dp: Dispatcher):
    await create_tables()
    await set_commands(dp)

    dp.setup_middleware(ThrottlingMiddleware())

if __name__ == '__main__':
    setup_logger("INFO", ["aiogram.bot.api"])

    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
