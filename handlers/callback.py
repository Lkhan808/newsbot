import datetime
import json

from aiogram import types
from aiogram.types import message

from config import dp


@dp.callback_query_handler(text="all news")
async def get_all_news(call: types.CallbackQuery):
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict):
        news = f"{datetime.datetime.fromtimestamp(v['news_datetime_stamp'])}\n{v['news_title']}\n{v['news_text']}" \
               f"\n{v['news_url']}"
        await message.answer(news)

