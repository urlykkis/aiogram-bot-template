from aiogram.types import Message

from loader import dp
from utils import IsAdmin


@dp.message_handler(IsAdmin(), commands=['admin'])
async def command_admin(message: Message):
    await message.answer("Админ-Меню")
