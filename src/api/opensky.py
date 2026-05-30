import requests
from nominatim import get_country_coordinates


def get_user_countries() -> list:
    """
    Запрашивает у пользователя 4 страны для отслеживания самолетов.

    Returns:
        list: список стран (строки)
    """
    countries = []

    print("Введите 4 страны для отслеживания самолетов:")

    for i in range(1, 5):
        country = input(f"Страна {i}: ").strip()
        countries.append(country)

    return countries


def get_states() -> list:
    """
    Получает текущее состояние самолетов из OpenSky Network API.

    Returns:
        list: список состояний самолетов (states)
    """
    url = "https://opensky-network.org/api/states/all"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    if "states" not in data:
        raise ValueError("В ответе нет ключа 'states'")

    return data["states"]


def filter_aircraft_by_country(
    states: list,
    lat: float,
    lon: float,
    radius: float = 5
) -> list:
    """
    Фильтрует самолеты по координатам страны (очень упрощенная модель).

    Args:
        states (list): список самолетов из OpenSky API
        lat (float): широта центра страны
        lon (float): долгота центра страны
        radius (float): допустимое отклонение по координатам

    Returns:
        list: список самолетов в заданной зоне
    """
    result = []

    for state in states:
        # OpenSky: state[5] = longitude, state[6] = latitude
        if state[5] is None or state[6] is None:
            continue

        if abs(state[6] - lat) <= radius and abs(state[5] - lon) <= radius:
            result.append(state)

    return result


if __name__ == "__main__":

    try:
        states = get_states()

        print("✔ Данные получены")
        print("Количество самолетов:", len(states))

        user_countries = get_user_countries()

        print("\n✔ Вы выбрали страны:", user_countries)

        for country in user_countries:
            lat, lon = get_country_coordinates(country)

            filtered = filter_aircraft_by_country(states, lat, lon)

            print(f"\n✈️ {country}")
            print("Самолётов в зоне:", len(filtered))

    except requests.exceptions.RequestException as e:
        print("Ошибка запроса:", e)

    except Exception as e:
        print("Общая ошибка:", e)
