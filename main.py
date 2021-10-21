import KeyHolder
import WeatherApi
import telebot
bot = telebot.TeleBot(KeyHolder.get_tg_key())


@bot.message_handler(content_types=['text'])
def get_text_messages(message):  # getting name city
    WeatherApi.get_weather(message.text)


bot.polling(none_stop=True, interval=0)
