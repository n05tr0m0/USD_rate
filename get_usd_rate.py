"""
Получение курса доллара с центрабанка в виде вспылвающего сообщения для Mac OS X

by n05tr0m0
"""

import pync
import requests
from bs4 import BeautifulSoup


def get_html():
    url = 'http://www.cbr.ru/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.142 Safari/537.36'
    }
    html_ = requests.get(url, headers=headers)
    return html_.text


def get_dollar_rate(html):
    soup = BeautifulSoup(html, 'lxml')
    tag_ = soup.find('ins', text='$').find_parent('tr').find_all('td')[-1].text
    clear_result = tag_.split()[-1]
    return clear_result


def send_message(message):
    title = 'Курс Доллара США'
    msg = message
    return pync.notify(f'На сегодня {msg[1:6]} руб.', title=title)


def main():
    send_message(get_dollar_rate(get_html()))


if __name__ == '__main__':
    main()
