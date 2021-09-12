import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def count_clicks(api_token, user_link):
    count_link = os.getenv("COUNT_LINK")
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
    short_link = os.getenv("SHORT_LINK")
    headers = {
        "Authorization": f"Bearer {api_token}",
    }
    manual_url = {
        "long_url": url,
    }
    response = requests.post(short_link, headers=headers, json=manual_url)
    response.raise_for_status()
    return response.json().get("link")


def is_bitlink(link):
    response = requests.get(link)
    response.raise_for_status()
    return response


def main():
    load_dotenv()
    bitly_token = os.getenv("BITLY_TOKEN")
    user_link = input("Пожалуйста, напишите url: ")
    try:
        (is_bitlink(user_link))
        print("Общее количество кликов =", count_clicks(
                                                        bitly_token, user_link
                                                        ))
    except requests.exceptions.HTTPError:
        print(shorten_link(bitly_token, user_link))


if __name__ == "__main__":
    main()
