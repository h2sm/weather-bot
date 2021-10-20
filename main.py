import requests
import KeyHolder
import TelegramBotHandler


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
    else:
        print("Неудачный запрос:" + str(resp.status_code))


def parse_response(resp):
    json_data = resp.json()
    for i in json_data:
        # print(i + " is a type of " + str(type(json_data[i])))
        if i == 'coord':
            coord_data = json_data[i]
            lon = coord_data.get("lon")
            lat = coord_data.get("lat")
        if i == 'weather':
            weather_data = json_data[i]
            list_weather_data = weather_data[0]
            main_weather = list_weather_data.get("main")
            weather_description = list_weather_data.get("description")
        if i == 'main':
            main_data = json_data[i]
            temp = main_data.get("temp")
            feels_like = main_data.get("feels_like")
            min_temp = main_data.get("temp_min")
            max_temp = main_data.get("temp_max")
        if i == 'name':
            city_name = json_data[i]


if __name__ == '__main__':
    get_weather()
