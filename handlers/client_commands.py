import datetime

from aiogram import types, Dispatcher
from client_keyboard.reply_kb import reply_keyboard
import json
from parsing.parsing import check_updates


async def get_started(message: types.Message):
    await message.answer("Здравствуйте, нужны новости?", reply_markup=reply_keyboard)


async def all_news(message: types.Message):
    with open("news_dict.json", encoding="utf-8") as file:
        news_dict: dict = json.load(file)
        for k, v in sorted(news_dict.items()):
            news = f"{datetime.datetime.fromtimestamp(v['news_datetime_stamp'])}\n" \
                   f"{v['news_title']}\n" \
                   f"{v['news_text']}\n" \
                   f"{v['news_url']}"
            await message.answer(news)


async def get_fresh_news(message: types.Message):
    fresh_news = check_updates()
    if len(fresh_news) >= 1:
            for k, v in sorted(fresh_news.items())[-5:]:
                news = f"{datetime.datetime.fromtimestamp(v['news_datetime_stamp'])}\n" \
                       f"{v['news_title']}\n" \
                       f"{v['news_text']}\n" \
                       f"{v['news_url']}"
                await message.answer(news)
    else:
        await message.answer("Свежих новостей пока нет")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(get_started, commands=["start"], commands_prefix="/!")
    dp.register_message_handler(all_news, commands=["allnews"])
    dp.register_message_handler(get_fresh_news, commands=["freshnews"])
