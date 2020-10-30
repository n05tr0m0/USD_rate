# Получение курса доллара

Получение курса доллара из центробанка в виде всплывающего сообщения для Mac OS X

#

![python](https://img.shields.io/badge/python-3.6%2B-blue) ![license](https://img.shields.io/badge/license-MIT-yellow)

### Установка

Склонируйте себе репозиторий: 

`https://github.com/n05tr0m0/usd_rate.git`

Создайте и активируйте виртуальное окружение:

`python3 -m venv <name_venv>`

`source <name_venv>/bin/activate`

Установите пакеты:

`pip install -r requirements.txt`

Запустите файл:

`python get_usd_rate.py`

Можно добавить запуск в crontab:

`00 12 * * * ~/USD_rate/<name_venv>/bin/python  ~/USD_rate/get_usd_rate.py`


Так же можно добавить алиас для вызова из терминала (пример для Mac OS):

OS Catalina: `nano .zprofile` <br>
`alias usd="~/USD_rate/<name_venv>/bin/python  ~/USD_rate/get_usd_rate.py"` 

<br>Предыдущие версии Mac OS X:
`nano .profile` <br>
`alias usd="~/USD_rate/<name_venv>/bin/python  ~/USD_rate/get_usd_rate.py"`


Enjoy!
