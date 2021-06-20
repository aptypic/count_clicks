import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import requests

load_dotenv()
short_link = "https://api-ssl.bitly.com/v4/shorten"
count_link = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary"
token = os.getenv("TOKEN")


def count_clicks(token, count_link, user_input):
    url = count_link.format(user_input)
    api_token = {
        "Authorization": f"Bearer {token}",
    }
    try:
        response = requests.get(url, headers=api_token)
        response.raise_for_status()
        return response.json().get("total_clicks")
    except requests.exceptions.HTTPError:
        print("Неверный формат (пример: bit.ly/3vds2)")


def shorten_link(token, short_link, url):
    api_token = {
        "Authorization": f"Bearer {token}",
    }
    manual_url = {
        "long_url": url,
    }
    try:
        response = requests.post(short_link, headers=api_token, json=manual_url)
        response.raise_for_status()
        return response.json().get("link")
    except requests.exceptions.HTTPError:
        print("Неверный формат (пример: https://gmail.com)")


def recognize_request():
    user_input = (input())
    parsing_input = urlparse(user_input)
    if parsing_input.scheme == "https" or parsing_input.scheme == "http":
        print(shorten_link(token, short_link, user_input))
    else:
        print("Общее количество кликов =", count_clicks(token, count_link, user_input))


def main():
    print("Пожалуйста, напишите url")
    recognize_request()


if __name__ == "__main__":
    main()
