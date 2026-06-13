from database.connection import get_connection


def insert_country(name, lat, lon):
    """
    Добавляет страну в таблицу countries.

    Если страна с таким именем уже существует,
    вставка игнорируется (ON CONFLICT DO NOTHING).

    Args:
        name (str): Название страны.
        lat (float): Географическая широта страны.
        lon (float): Географическая долгота страны.

    Returns:
        None

    Raises:
        psycopg2.Error: Возможные ошибки при работе с базой данных.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO countries(name, lat, lon)
                VALUES (%s, %s, %s)
                ON CONFLICT (name) DO NOTHING
                """,
                (name, lat, lon),
            )
