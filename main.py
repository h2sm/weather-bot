import requests

def get_city_name():
    print('Введите имя города по-английски')
    return input()

def get_weather():
    requests.get()

if __name__ == '__main__':
    city = get_city_name()

