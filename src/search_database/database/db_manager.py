"""
Модуль работы с базой данных.

Содержит класс DBManager для выполнения SQL-запросов к PostgreSQL
(страны и самолёты).
"""

import psycopg2

from src.search_database.config import DB_CONFIG


class DBManager:
    """
    Менеджер работы с базой данных PostgreSQL.

    Отвечает за получение соединения и выполнение SQL-запросов
    к таблицам countries и aeroplanes.
    """

    def __init__(self):
        """
        Инициализация соединения с базой данных.
        """
        self.conn = psycopg2.connect(**DB_CONFIG)

    def get_countries_and_aeroplanes_count(self):
        """
        Возвращает список стран и количество самолётов в каждой.

        Returns:
            list[tuple]: (название страны, количество самолётов)
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT c.name,
                       COUNT(a.id)
                FROM countries c
                LEFT JOIN aeroplanes a
                    ON c.id = a.country_id
                GROUP BY c.name
                ORDER BY c.name
            """)
            return cur.fetchall()

    def get_all_aeroplanes(self):
        """
        Возвращает все записи о самолётах.

        Returns:
            list[tuple]: все строки таблицы aeroplanes
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT *
                FROM aeroplanes
            """)
            return cur.fetchall()

    def get_avg_speed(self):
        """
        Вычисляет среднюю скорость самолётов.

        Returns:
            float | None: средняя скорость или None, если данных нет
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT AVG(speed)
                FROM aeroplanes
                WHERE speed IS NOT NULL
            """)
            return cur.fetchone()[0]

    def get_aeroplanes_with_higher_speed(self):
        """
        Возвращает самолёты со скоростью выше средней.

        Returns:
            list[tuple]: список самолётов
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT *
                FROM aeroplanes
                WHERE speed >
                (
                    SELECT AVG(speed)
                    FROM aeroplanes
                    WHERE speed IS NOT NULL
                )
            """)
            return cur.fetchall()

    def get_aeroplanes_with_keyword(self, keyword):
        """
        Ищет самолёты по ключевому слову в callsign.

        Args:
            keyword (str): часть позывного для поиска

        Returns:
            list[tuple]: найденные самолёты
        """
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT *
                FROM aeroplanes
                WHERE callsign ILIKE %s
            """,
                (f"%{keyword}%",),
            )
            return cur.fetchall()

    def close(self):
        """
        Закрывает соединение с базой данных.
        """
        self.conn.close()
