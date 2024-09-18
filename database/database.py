import logging
from typing import Union, Dict, List, Tuple


# Определяем типы данных
UserType = Dict[str, Any]  # Пользователь с произвольными атрибутами
ImageType = Dict[str, str]  # URL
CaptionType = Dict[str, str]  # Описание картинки
# Объединение типов
ValueType = UserType | ImageType | CaptionType
# База данных
DatabaseType = Dict[str, ValueType]

# Игрушечная база данных
class ToyDatabase:
    def __init__(self) -> None:
        self.database: DatabaseType = {}

# === Пользователи ===

    async def add_user(self, user_id: str, name: str) -> None:
        """Добавляет нового пользователя в базу данных."""
        if user_id in self.database:
            logging.debug(f"БД: Пользователь с ID {user_id} уже существует.")
            return
        
        self.database[user_id] = {
            "name": name
        }
        logging.debug(f"БД: Пользователь {name} добавлен.")

# === Картинки ===

# TODO дописать

# === Описание ===

# TODO дописать

# === Редактирование ===

    async def update_image(self, id: int, photo_id: str) -> None:
        try:
        # TODO дописать
        except Exception as e:
            logging.error(f"БД: Произошла ошибка: {e}")

    async def update_caption(self, id: int, caption: str) -> None:
        try:
        # TODO дописать
        except Exception as e:
            logging.error(f"БД: Произошла ошибка: {e}")


# Инициализируем игрушечную Базу Данных
MYDB = ToyDatabase()
