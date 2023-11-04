import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv

def shorten_link(token, link):
    url = "https://api-ssl.bitly.com/v4/shorten"
    params = {"long_url": link}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, bitlink):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    params = {"unit": 'month', 'units': -1}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, bitlink):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser(description='Программа помогает сокращать длинные ссылки и узнавать количество переходов по уже сокращенным ссылкам.')
    parser.add_argument('--url', type=str, help='Введите ссылку')
    args = parser.parse_args()
    parsed_url = urlparse(args.url)
    parsed_url = f"{parsed_url.netloc}{parsed_url.path}"
    try:
        if is_bitlink(token, parsed_url):
            print(count_clicks(token, parsed_url))
        else:
            print('Битлинк', shorten_link(token, args.url))
    except requests.exceptions.HTTPError:
        print('ОШИБКА, неправильная ссылка!')


if __name__ == '__main__':
    main()
