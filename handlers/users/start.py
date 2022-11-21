from aiogram.types import Message, ChatType

from loader import dp
from utils import select_user, register_user


@dp.message_handler(commands="start", chat_type=ChatType.PRIVATE)
async def command_start(message: Message):
    if await select_user(message.from_user.id) is None:
        await register_user(message.from_user.id)

    await message.answer("Меню пользователя")
