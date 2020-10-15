"""
Получение курса доллара с центробанка в виде всплывающего сообщения для Mac OS X

by n05tr0m0
"""

import pync
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError


def get_html_page() -> str:
    url = 'http://cbr.ru/'
    headers = {
        'user-agent': 'Mozilla/5.0 () AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 '
                      'OPR/67.0.3575.79'
    }

    try:
        resp = requests.get(url, headers=headers)
    except ConnectionError:
        resp = 'Нет соединения'

    return resp if isinstance(resp, str) else resp.text


def get_dollar_rate(source_text: str) -> str:
    if source_text == 'Нет соединения':
        return 'Нет соединения'
    soup = BeautifulSoup(source_text, 'lxml')
    result = soup.find('div', class_='indicator_el_value mono-num').text
    clear_result = result[:-3]
    return clear_result


def send_notification(message):
    if message == 'Нет соединения':
        return pync.notify('Невозможно получить данные', title='Ошибка сети')
    title = 'Доллара США по курсу ЦБ РФ'
    return pync.notify(f'На сегодня {message} руб.', title=title)


def main():
    send_notification(get_dollar_rate(get_html_page()))


if __name__ == '__main__':
    main()
