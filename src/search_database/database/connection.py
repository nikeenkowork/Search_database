import psycopg2

from src.search_database.config import DB_CONFIG


def get_connection():
    """
    Создаёт и возвращает соединение с базой данных PostgreSQL.

    Использует параметры подключения из конфигурации DB_CONFIG.

    Returns:
        psycopg2.extensions.connection: Объект соединения с PostgreSQL.

    Raises:
        psycopg2.OperationalError: Если не удалось установить соединение с БД.
    """
    return psycopg2.connect(**DB_CONFIG)
