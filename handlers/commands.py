import datetime
import json

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardRemove
from parsing.parsing import check_updates


async def start(message: types.Message):
    start_buttons = ["all news", "last 5 news", "Fresh news"]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("News tape", reply_markup=keyboard)


async def get_fresh_news(message: types.Message):
    fresh_news = check_updates()

    if len(fresh_news) >= 1:
        for k, v in sorted(fresh_news.items()):
            news = f"{datetime.datetime.fromtimestamp(v['news_datetime_stamp'])}\n" \
                   f"{(v['news_title'])}\n{(v['news_url'])}"
            await message.answer(news)
    else:
        await message.answer("пока нет свежих новостей")


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(get_fresh_news, commands=['fresh'])
