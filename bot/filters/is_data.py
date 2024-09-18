from aiogram.filters import BaseFilter
from aiogram.types import Message


class FilterIsData(BaseFilter):
    """Проверяем является ли текст сообщения одним из этих вариантов даты
    Примеры:
    10.05.2024
    9.12.2003
    12.5.2004
    3.5.2003

    return bool
    """
    async def __call__(self, message: Message) -> bool:
        # TODO написать фильтр
