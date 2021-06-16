import requests

url_template = "https://api-ssl.bitly.com/v4/shorten"
token = "7838b69b0b73672b305212bc8afcbce06e8f2e07"


def shorten_link(link):
    api_token = {
        "Authorization": f"Bearer {token}",
    }
    manual_url = {
        "long_url": link,
    }
    response = requests.post(url_template, headers=api_token, json=manual_url)
    response.raise_for_status()
    return response.json().get("link")


if __name__ == "__main__":
    print("Bitlink", shorten_link(input()))
