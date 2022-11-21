from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand, BotCommandScope, \
    BotCommandScopeType, BotCommandScopeDefault, BotCommandScopeChatAdministrators, BotCommandScopeAllGroupChats, \
    BotCommandScopeChat, BotCommandScopeChatMember

from utils.misc.config import Settings

default_commands = [
    BotCommand("start", "Запустить бота"),
]

admin_commands = [
    BotCommand("admin", "Админ-Меню"),
]


async def set_commands(dp: Dispatcher) -> None:
    await dp.bot.set_my_commands(default_commands, scope=BotCommandScopeDefault())

    await dp.bot.set_my_commands(
        admin_commands + default_commands,
        scope=BotCommandScopeChat(Settings.get_value("Bot", "admin_ids"))
    )
