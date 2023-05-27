import telebot
from telebot import types

tocken="6031800734:AAEGeTJwuYfoqzDe-Li2YC-_oQptvUpFfP8"
bot = telebot.TeleBot("6031800734:AAEGeTJwuYfoqzDe-Li2YC-_oQptvUpFfP8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Ласкаво прошу до розмови!")

@bot.message_handler(commands=['help'])
def send_infoHelp(message):
	text="/sitefmi -  перехід на сайт факультету" \
		 "/menu - виклик меню"
	bot.send_message(message.chat.id, "Це допомога!\n"+text)

@bot.message_handler(commands=['sitefmi'])
def send_infoUrlFmi(message):
	urlFMI="http://fmi-rshu.org.ua/"
	text=f'Сайт твого факультету доступний за посиланням <a href="{urlFMI}">Сайт ФМІ</a>'
	bot.send_message(message.chat.id, text,parse_mode='html')

@bot.message_handler(content_types=['photo'])
def send_photos(message):
	print(message)
	file_info=bot.get_file(message.photo[-1].file_id)
	print(file_info)
	downloaded_file=bot.download_file(file_info.file_path)
	bot.send_photo(message.chat.id,message.photo[-1].file_id)
	src = 'D:/2020_2021/' + file_info.file_path;
	with open(src, 'wb') as new_file:
		new_file.write(downloaded_file)
	bot.reply_to(message,"Фото завантажене")

@bot.message_handler(commands=['menu'])
def send_menu(message):
	murkup=types.InlineKeyboardMarkup()
	btn1=types.InlineKeyboardButton("Погода в Рівному",callback_data="parsPogoda")
	btn2 = types.InlineKeyboardButton("Курс долара", callback_data="parsDollar")
	murkup.add(btn1,btn2)
	bot.send_message(message.chat.id,"Виберіть пункт меню:",parse_mode='html',reply_markup=murkup)

@bot.callback_query_handler(func=lambda call:True)
def callback_woker(call):
	text_msg=""
	if call=="parsPogoda":
		text_msg=parsPogoda()
	elif call=="parsDollar":
		text_msg = parsDollar()
	bot.send_message(call.message.chat.id, text_msg)

def parsPogoda():
	pass

def parsDollar():
	pass

if __name__ == '__main__':
	bot.polling()