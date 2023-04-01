import json
from typing import Any

import requests
from pprint import pprint
from bs4 import BeautifulSoup, PageElement
from datetime import datetime
import time
import bs4

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
url = "https://www.securitylab.ru/news/"
request = requests.get(url=url, headers=headers)
soup = BeautifulSoup(request.text, "html.parser")
news_list = soup.find_all("a", class_="article-card inline-card")  # print(news_list)


def get_news():
    news_dict = {}
    for news in news_list:
        news_title = news.find("h2", class_="article-card-title").text.strip()
        news_text = news.find("p").text.strip()
        news_url = f"https://www.securitylab.ru/{news.get('href')}"
        news_date_time = news.find("time").get("datetime")
        iso_date = datetime.fromisoformat(news_date_time)
        date_time = datetime.strftime(iso_date, "%Y-%m-%d %H-%M-%S")
        news_datetime_stamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H-%M-%S").timetuple())
        news_id = news.get("id")
        news_dict[news_id] = {
            "news_datetime_stamp": news_datetime_stamp, "news_title": news_title,
            "news_text": news_text, "news_url": news_url
        }
        with open("news_dict.json", "w", encoding="utf-8") as newsfile:
            json.dump(news_dict, newsfile, indent=5, ensure_ascii=False)
        # print(f"{news_title}, {news_text}, {news_url}, {news_datetime_stamp}, {news_id}")


def check_updates():
    with open(r"C:\Users\Khan\PycharmProjects\pythonBOT TG\news_dict.json", encoding="utf-8") as file:
        news_dict = json.load(file)
        # print(news_list)
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
        }
        url = "https://www.securitylab.ru/news/"
        request = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(request.text, "html.parser")
        news_list = soup.find_all("a", class_="article-card inline-card")
        fresh_news = {}

        for news in news_list:
            news_url = f"https://www.securitylab.ru/{news.get('href')}"
            news_id = news.get("id")

            if news_id in news_dict:
                continue
            else:
                news_title = news.find("h2", class_="article-card-title").text.strip()
                news_text = news.find("p").text.strip()
                news_date_time = news.find("time").get("datetime")
                iso_date = datetime.fromisoformat(news_date_time)
                date_time = datetime.strftime(iso_date, "%Y-%m-%d %H-%M-%S")
                news_datetime_stamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H-%M-%S").timetuple())

                news_dict[news_id] = {
                    "news_datetime_stamp": news_datetime_stamp,
                    "news_title": news_title,
                    "news_text": news_text,
                    "news_url": news_url}

                fresh_news[news_id] = {
                    "news_datetime_stamp": news_datetime_stamp,
                    "news_title": news_title,
                    "news_text": news_text,
                    "news_url": news_url}
    with open("news_dict.json", mode="w", encoding="utf-8") as newsfile:
        json.dump(news_dict, newsfile, indent=5, ensure_ascii=False)
    return fresh_news


def main():
    # get_news()
    print(check_updates())
