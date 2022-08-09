"""
Получение курса доллара с центробанка в виде всплывающего сообщения для Mac OS X

Для регулярной проверки добавьте скрипт в crontab

by n05tr0m0
"""
import logging
from datetime import date, datetime
from json import JSONDecodeError
from typing import Any

import httpx
import pync

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('usd_rate.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def is_valid(input_data: dict[Any, Any]) -> bool:
    return all([
        len(input_data) == 2,
        input_data.get("data", False),
        isinstance(input_data.get("data"), datetime),
        input_data.get("curs", False),
        isinstance(input_data.get("curs"), float),
    ])


def get_usd_rate() -> dict[str, float | datetime]:
    url = 'https://cbr.ru/Queries/AjaxDataSource/112805'
    usd_params = {'DT': '', 'val_id': 'R01235'}
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/102.0.5005.167 Safari/537.36'}
    with httpx.Client() as client:
        try:
            resp = client.get(url, headers=headers, params=usd_params)
            result = resp.json()[0]
            result['data'] = datetime.strptime(result['data'], "%Y-%m-%dT%X")
            del result['diff']
            del result['prevDate']
            del result['NextWeekExist']
        except (httpx.HTTPError, httpx.HTTPStatusError, JSONDecodeError) as exc:
            logger.error(f'Нет доступа к сайту. Текст ошибки: {exc}')
            return {}
        save_backup_course(result)
        return result


def save_backup_course(input_data: dict[str, datetime | float]) -> None:
    with open('data', 'w', encoding='utf-8') as f:
        f.write(
            f'На {input_data.get("data", date.today()).strftime("%d.%m.%Y")} '
            f'курс доллара: {input_data.get("curs", 0):.2f} руб'
        )


def load_backup_course() -> str:
    with open('data', 'r', encoding='utf-8') as f:
        return f.read()


def send_notification(input_data: dict[str, datetime | float]) -> None:
    if is_valid(input_data):
        pync.notify(f'На сегодня {input_data.get("curs", 0):.2f} руб.', title="Доллара США по курсу ЦБ РФ")
    else:
        pync.notify(load_backup_course(), title='Нет сети. Последние сохранённые данные.')
        logger.error(f"Ошибка получения данных. Входящие данные: {input_data}")


def main():
    logger.info('Проверка курса доллара.')
    usd_rate = get_usd_rate()
    send_notification(usd_rate)
    logger.info('Проверка завершена.')


if __name__ == '__main__':
    main()
