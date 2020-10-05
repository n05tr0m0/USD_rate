# Получение курса доллара

Получение курса доллара с центрабанка в виде вспылвающего сообщения для Mac OS X

#

### Установка

Склонируйте себе репозиторий: 

`https://github.com/n05tr0m0/usd_rate.git`

Создайте и активируйте виртуальное окружение:

`python3 -m venv <name_venv>`

`source env/bin/activate`

Установите пакеты:

`pip install -r requirements.txt`

Запустите файл:

`python get_usd_rate.py`

Можено добавить запуск в crontab:

`00 12 * * * ~/USD_rate/env/bin/python  ~/USD_rate/get_usd_rate.py`


Так же можно добавить алиас для вызова из терминала (пример для Mac OS):

OS Catalina: `nano .zprofile` <br>
`alias usd="~/USD_rate/env/bin/python  ~/USD_rate/get_usd_rate.py"` 

<br>Предыдущие версии:
`nano .profile` <br>
`alias usd="~/USD_rate/env/bin/python  ~/USD_rate/get_usd_rate.py"`


Enjoy!
