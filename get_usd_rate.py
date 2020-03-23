"""
Получение курса доллара с центробанка в виде всплывающего сообщения для Mac OS X

by n05tr0m0
"""

import pync
import requests
from bs4 import BeautifulSoup


def get_html():
    url = 'http://cbr.ru/'
    headers = {
        'user-agent': 'Mozilla/5.0 () AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 '
                      'OPR/67.0.3575.79'
    }
    html_ = requests.get(url, headers=headers)
    return html_.text


def get_dollar_rate(html):
    soup = BeautifulSoup(html, 'lxml')
    result = soup.find('div', class_='indicator_el_value mono-num').text
    clear_result = result[:-3]
    return clear_result


def send_notification(message):
    title = 'Курс Доллара США'
    return pync.notify(f'На сегодня {message} руб.', title=title)


def main():
    send_notification(get_dollar_rate(get_html()))


if __name__ == '__main__':
    main()
