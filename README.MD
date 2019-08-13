# Получение курса доллара

Получение курса доллара с центрабанка в виде вспылвающего сообщения для Mac OS X

#

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

Можено добавить запуск в crontab:

`00 12 * * * ~/<username>/<name_venv>/bin/python  ~/<username>/USD_rate/get_usd_rate.py`


Enjoy!
