import os

from dotenv import load_dotenv
from urllib.parse import urlparse
import requests



def count_clicks(count_link, headers, a):
    b = urlparse(a)
    b = b._replace(scheme='')
    a = b.geturl()
    url = count_link.format(a)
    api_token = {
        "Authorization": f"Bearer {headers}",
    }
    response = requests.get(url, headers=api_token)
    response.raise_for_status()
    return response.json().get("total_clicks")


def shorten_link(headers, short_link, url):
    api_token = {
        "Authorization": f"Bearer {headers}",
    }
    manual_url = {
        "long_url": url,
    }
    response = requests.post(short_link, headers=api_token, json=manual_url)
    response.raise_for_status()
    return response.json().get("link")


def main():
    load_dotenv()
    token_bitly = os.getenv("TOKEN")
    count_link = os.getenv("count_link")
    short_link = os.getenv("short_link")
    print("Пожалуйста, напишите url")
    a = input()
    try:
        print("Общее количество кликов =", count_clicks(count_link,
                                                        token_bitly, a))
    except requests.exceptions.HTTPError:
        print(shorten_link(token_bitly, short_link, a))


if __name__ == "__main__":
    main()
