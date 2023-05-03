from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from aiogram.utils.markdown import text, escape_md
from datetime import datetime
from aiogram.utils.markdown import Text
from aiogram.types import InputMediaPhoto
from aiogram.utils.html import quote_html

from database import get_user_city, set_user_city
from ics_calendar import get_ics_calendar, get_events_by_date
from config import AVAILABLE_CITIES

async def start(message: types.Message):
    await message.reply("Добро пожаловать! Пожалуйста, введите название города:")

async def choose_city(message: types.Message, state: FSMContext):
    city_name = message.text
    if city_name not in AVAILABLE_CITIES:
        await message.reply("Город не найден. Пожалуйста, введите название города снова:")
        return
    calendar = get_ics_calendar(AVAILABLE_CITIES[city_name])
    set_user_city(user_id=message.from_user.id, city=city_name)

    await state.set_state('date')
    await message.reply("Выберите дату в формате ГГГГ-ММ-ДД:")

async def process_date(message: types.Message, state: FSMContext):
    if await state.get_state() != 'date':
        return

    try:
        date = datetime.strptime(message.text, "%Y-%m-%d")
    except ValueError:
        await message.reply("Некорректный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД:")
        return

    city_name = get_user_city(user_id=message.from_user.id)
    calendar = get_ics_calendar(AVAILABLE_CITIES[city_name])
    events = get_events_by_date(calendar=calendar, date=date)

    if not events:
        await message.reply("На выбранную дату событий не найдено.")
    else:
        for event in events:
            title = f"*{quote_html(event['summary'])}*"
            description = quote_html(event["description"])
            url = event["url"]
            image_url = event["image_url"]

            caption = f"{title}\n{description}\n[{quote_html('Перейти на сайт события')}]({url})"
            media = InputMediaPhoto(media=image_url, caption=caption, parse_mode=ParseMode.HTML)

        await message.reply_photo(photo=image_url, caption=caption, parse_mode=ParseMode.HTML)

    await state.finish()
