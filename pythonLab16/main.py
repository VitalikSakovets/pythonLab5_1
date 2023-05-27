import telebot
from telebot import types

import requests
from bs4 import BeautifulSoup
from lxml import html

token = '6031800734:AAEGeTJwuYfoqzDe-Li2YC-_oQptvUpFfP8'
bot = telebot.TeleBot(token)
# @bot.message_handlers(commands=['start','help'])
@bot.message_handler(commands=["start","help"])
def start(message):
    # print(message)
    # bot.send_message(message.chat.id, 'Привіт')
    keyboard = types.ReplyKeyboardMarkup(row_width=True)
    a1 = types.KeyboardButton('Дізнатися погоду в місті Рівне')
    a2 = types.KeyboardButton('Офіційний курс гривні щодо іноземних валют')
    keyboard.add(a1, a2)
    bot.send_message(message.chat.id,'Натиснути кнопку start',reply_markup=keyboard)
    # bot.send_message(message.chat.id,f'Привіт{message.from_use.first_name}\n\nid:{message.from_user.id}\nusername: {message.from_user.username}',reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Дізнатися погоду в місті Рівне':
        # bot.send_message(message.chat.id, '⛅️')
        bot.send_message(message.chat.id, f'Погода{weather()}')
    elif message.text == 'Офіційний курс гривні щодо іноземних валют':
        # bot.send_message(message.chat.id, '💰')
        keyboarde = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardMarkup('USD', callback_data='840')
        b2 = types.InlineKeyboardMarkup('PL', callback_data='985')
        b3 = types.InlineKeyboardMarkup('EUR', callback_data='978')
        keyboarde.add(b1, b2, b3)
        bot.send_message(message.chat.id,f'Курс {currency()}',reply_markup=keyboarde)
        currency('a')
    # else:
    #     bot.send_message(message.chat.id, 'Невідома команда')


@bot.callback_query_handler(func=lambda call: True)
def main(call):
    if call.data == '840' or call.data == '985' or call.data == '978':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, f'ОФіційний курс на сьогодні {currency(call.data)}')
    else:
        bot.send_message(call.message.chat.id, 'Невідома команда')

def weather():
    url = requests.get(
        'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%80%D1%96%D0%B2%D0%BD%D0%B5/2023-05-26')
    print(url.status_code)
    soup = BeautifulSoup(url.text, 'lxml')
    temp = soup.find('p', {'class': 'today-temp'}).text
    return temp


def currency(val):
    url = requests.get('https://bank.gov.ua/ua/markets/exchangerates')
    print(url.status_code)
    soup = BeautifulSoup(url.text, 'lxml')
    rows = soup.find_all('tr')
    for row in rows:
        try:
            code_element = row.find('td', {'class': 'hidden-sm'})
            rate_element = row.find('td', {'data-label': 'Офіційний курс'})
            code = int(code_element.find('span', {'class' : 'value'}).text)
            rate = rate_element.text
            print(rate)
            if val == code:
                return rate
        except:
            pass
    return None


@bot.message_handler(content_types=['voice'])
def voice(message):
    bot.reply_to(message, 'this is voice')


@bot.message_handler(content_types=['photo', 'document'])
def photo(message):
    bot.reply_to(message, 'this is photo')


@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.reply_to(message, 'this is sticker')

if __name__ == '__main__':
    bot.polling()



























# import telebot
# from telebot import types
#
# import requests
# from bs4 import BeautifulSoup
# from lxml import html
#
# token = '6031800734:AAEGeTJwuYfoqzDe-Li2YC-_oQptvUpFfP8'
# bot = telebot.TeleBot(token)
# # @bot.message_handlers(commands=['start','help'])
# @bot.message_handler(commands=["start","help"])
# def start(message):
#     # print(message)
#     # bot.send_message(message.chat.id, 'Привіт')
#     keyboard = types.ReplyKeyboardMarkup(row_width=True)
#     a1 = types.KeyboardButton('Дізнатися погоду в місті Рівне')
#     a2 = types.KeyboardButton('Офіційний курс гривні щодо іноземних валют')
#     keyboard.add(a1, a2)
#     # bot.send_message(message.chat.id,'Натиснути кнопку start',reply_markup=keyboard)
#     bot.send_message(message.chat.id,f'Привіт{message.from_use.first_name}\n\nid:{message.from_user.id}\nusername: {message.from_user.username}',reply_markup=keyboard)
#
#
# @bot.message_handler(content_types=['text'])
# def text(message):
#     if message.text == 'Дізнатися погоду в місті Рівне':
#         bot.send_message(message.chat.id, '⛅️')
#         bot.send_message(message.chat.id, f'Погода{weather()}')
#     elif message.text == 'Офіційний курс гривні щодо іноземних валют':
#         bot.send_message(message.chat.id, '💰')
#         keyboarde = types.InlineKeyboardMarkup()
#         b1 = types.InlineKeyboardMarkup('USD', callback_data='840')
#         b2 = types.InlineKeyboardMarkup('PL', callback_data='985')
#         b3 = types.InlineKeyboardMarkup('EUR', callback_data='978')
#         keyboarde.add(b1, b2, b3)
#         bot.send_message(message.chat.id, f'Виберіть доступну валюту: ', reply_markup=keyboarde)
#     else:
#         bot.send_message(message.chat.id, 'Невідома команда')
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def main(call):
#     if call.data == '840' or call.data == '985' or call.data == '978':
#         bot.delete_message(call.message.chat.id, call.message.id)
#         bot.send_message(call.message.chat.id, f'ОФіційний курс на сьогодні {currency(call.data)}')
#     else:
#         bot.send_message(call.message.chat.id, 'Невідома команда')
#
# def weather():
#     url = requests.get(
#         'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%80%D1%96%D0%B2%D0%BD%D0%B5/2023-05-26')
#     print(url.status_code)
#     soup = BeautifulSoup(url.text, 'lxml')
#     temp = soup.find('p', {'class': 'today-temp'}).text
#     return temp
#
#
# def currency(val):
#     url = requests.get('https://bank.gov.ua/ua/markets/exchangerates')
#     print(url.url)
#     soup = BeautifulSoup(url.text, 'lxml')
#     rows = soup.find_all('tr')
#     for row in rows:
#         try:
#             code_element = row.find('td', {'class': 'hidden-sm'})
#             rate_element = row.find('td', {'date_label': 'Офіційний курс'})
#             code = code_element.text
#             rate = rate_element.text
#             if val == code:
#                 return rate
#         except:
#             pass
#     return None
#
#
# @bot.message_handler(content_types=['voice'])
# def voice(message):
#     bot.reply_to(message, 'this is voice')
#
#
# @bot.message_handler(content_types=['photo', 'document'])
# def photo(message):
#     bot.reply_to(message, 'this is photo')
#
#
# @bot.message_handler(content_types=['sticker'])
# def sticker(message):
#     bot.reply_to(message, 'this is sticker')
#
# if __name__ == '__main__':
#     bot.polling()
