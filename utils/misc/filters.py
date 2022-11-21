from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from .config import Settings


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return str(message.from_user.id) in Settings.get_admins()
