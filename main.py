import requests
import KeyHolder


def get_city_name():
    print('Введите имя города по-английски')
    return input()


def get_api_key():
    return KeyHolder.get_key()


def get_weather():
    key = get_api_key()
    city = get_city_name()
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric" + "&appid=" + key
    resp = requests.get(url)
    if resp.status_code == 200:
        parse_response(resp)


def parse_response(resp):
    print('e')


if __name__ == '__main__':
    get_weather()
