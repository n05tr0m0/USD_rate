"""
Получение курса доллара с центробанка в виде всплывающего сообщения для Mac OS X

by n05tr0m0
"""
import logging
import re
from datetime import date

import pync
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('usd_rate.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def get_html_page() -> str or None:
    url = 'http://cbr.ru/'
    headers = {
        'user-agent': 'Mozilla/5.0 () AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 '
                      'OPR/67.0.3575.79'
    }

    try:
        resp = requests.get(url, headers=headers)
    except ConnectionError as err:
        logger.warning(f'Нет доступа к сайту по сети. Текст ошибки: {err}')
        resp = 'Нет соединения'

    return resp if isinstance(resp, str) else resp.text


def save_last_course(usd_value: str):
    with open('data', 'w', encoding='utf-8') as f:
        f.write(f'На {date.today().strftime("%d.%m.%Y")} курс доллара: {usd_value} руб')


def get_dollar_rate(source_text: str) -> str:
    if source_text == 'Нет соединения':
        return 'Нет соединения'
    soup = BeautifulSoup(source_text, 'lxml')
    try:
        result = soup.find('div', class_='col-md-2 col-xs-9 _right mono-num').text
    except AttributeError as err:
        logger.warning(f'Скорее всего слетела вёрстка сайта. Текст ошибки: {err}')
        return 'Нет результата'
    clear_result = re.match(r'\d{2},\d{2}', result).group(0)
    save_last_course(clear_result)
    return clear_result


def load_last_course() -> str:
    with open('data', 'r', encoding='utf-8') as f:
        return f.read()


def send_notification(message):
    if message == 'Нет соединения' or message == 'Нет результата':
        try:
            last_course = load_last_course()
        except FileNotFoundError:
            return pync.notify('Невозможно получить данные', title='Ошибка')
        return pync.notify(last_course, title='Нет сети. Последние сохранённые данные.')
    title = 'Доллара США по курсу ЦБ РФ'
    return pync.notify(f'На сегодня {message} руб.', title=title)


def main():
    logger.info('Проверка курса доллара.')
    send_notification(get_dollar_rate(get_html_page()))
    logger.info('Проверка завершена.')


if __name__ == '__main__':
    main()
