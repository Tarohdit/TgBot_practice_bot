# Архитектура бота
# https://drive.google.com/file/d/1adZOktmbXmGQZN6JAQi4btxkyCHCbvev/view?usp=sharing
# Открыть с помощью draw.io
# Для перемещения "пробел + ЛКМ", для масштабирования "пробел + колесо мышки"

# Полезная информация по созданию ботов
# https://mastergroosha.github.io/aiogram-3-guide/
# https://stepik.org/lesson/744814/step/1?unit=746585
# (stepik.org - использовать 'меню' для перехода между темами и 'квадратики' для перехода к след. шагу темы)

from dotenv import load_dotenv
print('Загружаем переменные окружения')
load_dotenv()

import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.commands.main_menu import set_main_menu
from bot.handlers import (
    owner,
    user,
    update_handler
)
from bot.handlers.callback_query import owner_callback


async def main():
    
    BOT_TOKEN=getenv("BOT_TOKEN")
    # Инициализируем бот и диспетчер
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()  # TODO подключить хранилище

    # Настраиваем меню команд
    await set_main_menu(bot)

    # Регистрируем роутеры в диспетчере, включаем маршрутизаторы

    # Владелец
    dp.include_router(owner.router)
    # Пользователи
    dp.include_router(user.router)
    # Callback
    # TODO подключить нужные маршрутизаторы

    # Ловим все оставшиеся update
    dp.include_router(update_handler.router)

    # Пропускаем накопившиеся update (обновления)
    await bot.delete_webhook(drop_pending_updates=True)

    # запускаем (опрос сервера на наличие обновлений)
    await dp.start_polling(bot)


def log_config():
    # Настраиваем логирование
    logging.basicConfig(
        level=logging.DEBUG,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(funcName)s",  # Формат сообщения
        handlers=[
            logging.FileHandler('app.log', mode='w', encoding='utf-8'),  # Файл для записи логов
            logging.StreamHandler(sys.stdout)  # Вывод логов в консоль
        ],
    )
    # Получаем корневой логгер
    logger = logging.getLogger()
    # Получаем эффективный уровень логирования
    level = logger.getEffectiveLevel()
    # Преобразуем уровень в строку
    level_name = logging.getLevelName(level)
    logging.debug(f'Текущий уровень логирования: {level_name}')


if __name__ == "__main__":
    try:
        log_config()
        logging.info('=== BOT START ===')
        asyncio.run(main())
    except KeyboardInterrupt:
        # Чтобы не мусорить в командной строке при остановке программы вручную (Ctrl+C)
        logging.info('=== BOT STOP ===')
