from aiogram import Bot
from aiogram.types import BotCommand

from bot.text.text_ru import TEXT_COMMANDS_RU


async def set_main_menu(bot: Bot):
    """Автоматическая настройка меню команд бота"""
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in TEXT_COMMANDS_RU.items()
    ]
    await bot.set_my_commands(main_menu_commands)
