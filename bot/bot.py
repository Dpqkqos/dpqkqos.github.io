import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests

# Инициализация бота
bot = Bot(token="YOUR_TELEGRAM_BOT_TOKEN")
dp = Dispatcher()

@dp.message(commands=['start'])
async def cmd_start(message: types.Message):
    # Создание кнопок
    keyboard = InlineKeyboardMarkup()

    # Кнопка для открытия веб-приложения
    button_open_app = InlineKeyboardButton(
        text="Перейти на страницу состояния",
        url="https://yourproject.herokuapp.com/user-state/{}".format(message.chat.id)
    )
    
    # Кнопка для записи состояния
    button_record_state = InlineKeyboardButton(
        text="Записать свое состояние",
        callback_data="record_state_{}".format(message.chat.id)
    )

    keyboard.add(button_open_app, button_record_state)
    await message.answer("Привет! Выберите действие:", reply_markup=keyboard)

# Обработчик для записи состояния
@dp.callback_query_handler(lambda c: c.data.startswith('record_state_'))
async def record_state(callback_query: types.CallbackQuery):
    chat_id = callback_query.data.split("_")[2]
    await bot.send_message(chat_id, "Напишите ваше состояние:")

# Обработчик для сохранения состояния
@dp.message(lambda message: message.text and not message.text.startswith('/'))
async def handle_state(message: types.Message):
    chat_id = str(message.chat.id)
    state = message.text
    response = requests.post(
        "http://localhost:8000/api/user-state/",
        data={"chat_id": chat_id, "state": state}
    )
    if response.status_code == 200:
        await message.answer("Ваше состояние успешно записано!")
    else:
        await message.answer("Произошла ошибка при записи состояния.")

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())