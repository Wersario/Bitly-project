import requests
import argparse
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
load_dotenv()


def shorten_url(url, token):
    initial_url = "https://api-ssl.bitly.com/v4/shorten"

    headers = {
        "Authorization": token
    }

    json_params = {
        "long_url": url
    }

    response = requests.post(initial_url, headers=headers, json=json_params)
    response.raise_for_status()
    bitlink = response.json()['link']

    return bitlink


def count_clicks(bitlink, token):
    path = urlparse(bitlink).netloc + urlparse(bitlink).path
    initial_url = f"https://api-ssl.bitly.com/v4/bitlinks/{path}/clicks/summary"

    headers = {
        "Authorization": token
    }

    response = requests.get(initial_url, headers=headers)
    response.raise_for_status()
    clicks_amount = response.json()['total_clicks']
    return clicks_amount


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ввод значений')
    parser.add_argument('link', help='Ссылка, с которой вы работаете')
    args = parser.parse_args()
    url = args.link
    try:
        clicks = count_clicks(url, os.getenv('BITLY_TOKEN'))
        print(clicks)
    except requests.exceptions.HTTPError:
        try:
            bitlink = shorten_url(url, os.getenv('BITLY_TOKEN'))
            print(bitlink)
        except requests.exceptions.HTTPError:
            print("You wrote something incorrectly")
