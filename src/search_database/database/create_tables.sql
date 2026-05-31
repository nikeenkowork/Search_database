/*
Таблица стран.

Хранит справочник стран с координатами.

Поля:
    id       — уникальный идентификатор (PK)
    name     — название страны (уникальное, обязательное)
    lat      — широта
    lon      — долгота
*/
CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    lat NUMERIC,
    lon NUMERIC
);

/*
Таблица самолетов.

Хранит данные о самолетах и их текущем состоянии.

Поля:
    id           — уникальный идентификатор (PK)
    icao24       — уникальный ICAO идентификатор самолета
    callsign     — позывной
    country_id   — ссылка на страну (FK -> countries.id)
    longitude    — долгота
    latitude     — широта
    speed        — скорость
    altitude     — высота
*/
CREATE TABLE aeroplanes (
    id SERIAL PRIMARY KEY,
    icao24 VARCHAR(20) UNIQUE,
    callsign VARCHAR(20),
    country_id INTEGER REFERENCES countries(id),
    longitude NUMERIC,
    latitude NUMERIC,
    speed NUMERIC,
    altitude NUMERIC
);
