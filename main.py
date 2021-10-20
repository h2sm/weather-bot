import requests
import KeyHolder
import json


def get_city_name():
    print('Введите имя города по-английски')
    return input()


def get_api_key():
    return KeyHolder.get_key()


def get_weather():
    key = get_api_key()
    city = get_city_name()
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric" + "&appid=" + key
    print(url)
    resp = requests.get(url)
    if resp.status_code == 200:
        parse_response(resp)
    else:
        print('Неудачный запрос: ' + resp.status_code)


def parse_response(resp):
    json_data = resp.json()
    if 'weather' in json_data:
        print(json_data["weather"])


if __name__ == '__main__':
    get_weather()
