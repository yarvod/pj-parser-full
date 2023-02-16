# phystech.job full parser of telegram channels

## Необходимое ПО

* python3
* git

## Установка

1. Клонируйте репозиторий
    ```
    git clone https://github.com/yarvod/pj-parser-full.git
    ```
2. Создайте виртуальное окружение:
    ```
    python3 -m venv venv
    ```
3. Активируйте окружение:
    ```
    source venv/bin/activate
    ```
4. Установите зависимости:
    ```
    pip3 install -r requirements.txt
    ```
5. Создайте `.env` файл и положите в корневую папку с проектом
6. Положите в `.env` файл номер телефона:
    ```
    PHONE=...
    ```
7. Создайте приложение в телеграмме через https://my.telegram.org/apps
8. Возьмите полученные api_id и api_hash и положите в `.env` файл
   ```
   API_ID=...
   API_HASH=...
   ```
9. Запустите скрипт:
   ```
   python bot.py -c {channel name} -l {number of posts}
   ```
   Понадобиться ввести номер код из телеграмма.
10. В файле `data.json` будет лежать полученные данные.
