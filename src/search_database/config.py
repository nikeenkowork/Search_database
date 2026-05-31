import os

from dotenv import load_dotenv

"""
Конфигурация подключения к базе данных.

Загружает переменные окружения из файла .env и формирует словарь
с параметрами подключения к PostgreSQL.

Переменные окружения:
    DB_NAME: Название базы данных.
    DB_USER: Имя пользователя.
    DB_PASSWORD: Пароль пользователя.
    DB_HOST: Адрес сервера базы данных.
    DB_PORT: Порт подключения.
"""

load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}
