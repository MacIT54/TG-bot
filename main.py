import requests
import telebot
from telebot import types

bot = telebot.TeleBot("5371485154:AAGJmc2o_l0P4vrL3KTdxNW9Yq_hu-987kY")

url = 'https://api.exchangerate.host/latest/USD'
response = requests.get(url).json()
data = response.get('rates')
print(data)

def keys(key):
    if key in data:
        return data.get(key)
    else:
        return print(f"There is no such currency in our database")

@bot.message_handler(content_types=['text'])
def message_reply(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Show exchange rates")
    item2 = types.KeyboardButton("Show financial news")
    item3 = types.KeyboardButton("help")
    markup.add(item1, item2, item3)
    if message.text == "Show exchange rates":
        bot.send_message(message.chat.id, f"Enter currency code. For example: USD, EUR, RUB",
                         reply_markup=markup)
    elif message.text in data:
        ms = f'{message.text}'
        bot.send_message(message.chat.id, keys(ms), reply_markup=markup)
    elif message.text == "Show financial news":
        bot.send_message(message.chat.id, f"This function in development", reply_markup=markup)
    elif message.text == "start":
        bot.send_message(message.chat.id, f"Hi there, {message.from_user.first_name}. Welcome to my first TGbot. He's able show exchange rates and financial news"
                         f", choose what you would like to do:", reply_markup=markup)
    elif message.text == "help":
        bot.send_message(message.chat.id, f"Commands: start, help, Show exchange rates, Show financial news", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"This command was not recognized", reply_markup=markup)

bot.polling(none_stop=True)







