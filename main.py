import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import BotCommand
from aiogram.utils import executor
from aiogram.contrib.middlewares.fsm import FSMMiddleware
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from memory_storage import MemoryStorage
from aiogram.dispatcher.filters import Text
from telegram_handlers import start, choose_city, process_date

from config import API_TOKEN, AVAILABLE_CITIES
from database import create_tables, close_db

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())  # добавить storage=MemoryStorage() в этой строке

dp.middleware.setup(LoggingMiddleware())
dp.middleware.setup(FSMMiddleware())

dp.register_message_handler(start, Command("start"))
dp.register_message_handler(choose_city, Text(equals=AVAILABLE_CITIES.keys(), ignore_case=True), state='*')
dp.register_message_handler(process_date, state='date')

create_tables()
executor.start_polling(dp, skip_updates=True, on_shutdown=close_db)
