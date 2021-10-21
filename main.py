import KeyHolder
import WeatherApi
import telebot

bot = telebot.TeleBot(KeyHolder.get_tg_key())


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,
                     "Напишите название города, и я вам скажу какая там погода! Желательно по-английски")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):  # getting name city
    weather_report = WeatherApi.get_weather(message.text)
    bot.send_message(message.from_user.id, weather_report)


bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    start()
