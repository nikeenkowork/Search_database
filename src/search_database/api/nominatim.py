import requests


def get_country_coordinates(country: str) -> tuple[float, float]:
    """
    Возвращает координаты страны (lat, lon) через Nominatim API.
    """

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": country,
        "format": "json",
        "limit": 1,
    }

    headers = {"User-Agent": "geo-coordinates-app"}

    response = requests.get(url, params=params, headers=headers, timeout=10)

    # 1. Проверяем HTTP-статус
    if response.status_code == 200:
        print("✔ Сервер успешно вернул данные")
    else:
        print(f"✖ Ошибка сервера: {response.status_code}")

    response.raise_for_status()

    # 2. Получение JSON-ответа от сервера и преобразование его в Python-объект (dict/list)
    data = response.json()

    # 3. Проверяем, что данные не пустые
    if not data:
        raise ValueError(f"Сервер не нашёл данные по стране: {country}")

    # 4. Подтверждение, что данные реально получены
    print(f"✔ Получено {len(data)} результат(ов) от сервера")

    # 5. Возвращаем координаты
    return float(data[0]["lat"]), float(data[0]["lon"])
    # Возвращает координаты первой найденной локации:
    # lat — широта (latitude), lon — долгота (longitude)
    # data[0] — первый результат от Nominatim API
    # значения преобразуются из строк в float


# ИНИЦИАЛИЗАЦИЯ
if __name__ == "__main__":
    result = get_country_coordinates("Czech Republic")
    print(result)
