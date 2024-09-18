from aiogram import Router
from aiogram.types import Message
from aiogram.types import CallbackQuery


router = Router(name=__name__)


# Этот маршрутизатор ловит все оставшиеся обновления, нужен для тестов
@router.message()
async def update_info_message(message: Message):
    # покажет объект типа Message в JSON-формате для анализа update
    update_message = message.model_dump_json(
        indent=8,  # кол-во пробелов в отступе для JSON
        exclude_none=True  # если True, пропускает все поля со значением None
    )
    print('update_handler_start')
    print(update_message)
    print('update_handler_end')


@router.callback_query()
async def update_info_callback(callback: CallbackQuery):
    update_callback = callback.model_dump_json(
        indent=8,
        exclude_none=True
    )
    print(update_callback)
    await callback.answer()
