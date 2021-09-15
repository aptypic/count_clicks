import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def count_clicks(api_token, user_link):
    count_link = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary"
    url_parse = urlparse(user_link)
    url_parse = url_parse._replace(scheme="")
    user_link = url_parse.geturl()
    url = count_link.format(user_link)
    headers = {
        "Authorization": f"Bearer {api_token}",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get("total_clicks")


def shorten_link(api_token, url):
    short_link = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {api_token}",
    }
    manual_url = {
        "long_url": url,
    }
    response = requests.post(short_link, headers=headers, json=manual_url)
    response.raise_for_status()
    return response.json().get("link")


def is_bitlink(api_token, link):
    info_link = "https://api-ssl.bitly.com/v4/bitlinks/{}"
    headers = {
        "Authorization": f"Bearer {api_token}",
    }
    url_parse = urlparse(link)
    url_parse = url_parse._replace(scheme="")
    user_link = url_parse.geturl()
    url = info_link.format(user_link)
    response = requests.get(url, headers=headers)
    return response.ok


def recognize_link(bitly_token, user_link):
    try:
        if is_bitlink(bitly_token, user_link):
            print(
                 "Общее количество кликов =",
                 count_clicks(bitly_token, user_link))
        else:
            print(shorten_link(bitly_token, user_link))
    except requests.exceptions.HTTPError:
        print("Укажите верную ссылку")


def main():
    load_dotenv()
    bitly_token = os.getenv("TOKEN")
    user_link = input("Пожалуйста, напишите url: ")
    recognize_link(bitly_token, user_link)


if __name__ == "__main__":
    main()
