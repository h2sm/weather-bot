import requests
import KeyHolder


def get_weather(cityname):
    key = KeyHolder.get_weather_api_key()
    city = cityname
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric" + "&appid=" + key
    resp = requests.get(url)
    if resp.status_code == 200:
        return parse_response(resp)
    else:
        return "Неудачный запрос:" + str(resp.status_code)


def parse_response(resp):
    json_data = resp.json()
    for i in json_data:
        # print(i + " is a type of " + str(type(json_data[i])))
        if i == 'coord':
            coord_data = json_data[i]
            lon = str(coord_data.get("lon"))
            lat = str(coord_data.get("lat"))
        if i == 'weather':
            weather_data = json_data[i]
            list_weather_data = weather_data[0]
            main_weather = list_weather_data.get("main")
            weather_description = list_weather_data.get("description")
        if i == 'main':
            main_data = json_data[i]
            temp = str(main_data.get("temp"))
            feels_like = str(main_data.get("feels_like"))
            min_temp = str(main_data.get("temp_min"))
            max_temp = str(main_data.get("temp_max"))
        if i == 'name':
            city_name = json_data[i]

    return "Weather in " + city_name + "(" + lon + "," + lat + "): " \
           + main_weather + ", description - " + weather_description + ". Temp is " + temp + \
           ", feels like " + feels_like + ", minimum is " + min_temp + ", max is " + max_temp
