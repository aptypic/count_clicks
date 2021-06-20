import requests

short_link = "https://api-ssl.bitly.com/v4/shorten"
count_link = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary"
token = "7838b69b0b73672b305212bc8afcbce06e8f2e07"


def count_clicks(token, count_link):
    url = count_link.format(input())
    api_token = {
        "Authorization": f"Bearer {token}",
    }
    try:
        response = requests.get(url, headers=api_token)
        response.raise_for_status()
        return response.json().get("total_clicks")
    except requests.exceptions.HTTPError:
        print("Неверный формат (пример: bit.ly/3vds2)")


def shorten_link(token, short_link):
    url = input()
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


def main():
    print("Пожалуйста, напишите url")
    # print(shorten_link(token, short_link))
    print("Общее количество кликов =", count_clicks(token, count_link))


if __name__ == "__main__":
    main()
