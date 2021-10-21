def get_weather_api_key():
    f = open("KEY.txt", "r")
    return f.read()


def get_tg_key():
    f = open("tgkey.txt", "r")
    return f.read()
