#python D:\pypro\tgbot\bot.py
import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('D:/pypro/tgbot/pic/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Понедельник")
	item2 = types.KeyboardButton("Вторник")
	item3 = types.KeyboardButton("Среда")
	item4 = types.KeyboardButton("Четверг")
	item5 = types.KeyboardButton("Пятница")


	markup.add(item1, item2, item3, item4, item5)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def schedule(message):
	if message.chat.type == 'private':
		if message.text == 'Понедельник':
			bot.send_message(message.chat.id, 'Веб-тех(лб)\nОССП(лек)\nРазработка ПИ(лек)\nТеория инф(лек)')
		elif message.text == 'Вторник':
			bot.send_message(message.chat.id, '/Веб-тех(лек)\nКомп СС(лаб)\nОТ(лек)/ООТПСП(лек)\n/Теория инф(лек)')
		elif message.text == 'Среда':
			bot.send_message(message.chat.id, 'ТРПО\nОССП(лек)\nОССП(лаб)\nРазработка ПИ(прак)/')
		elif message.text == 'Четверг':
			bot.send_message(message.chat.id, 'ООТПСП(лек)\nОТ(прак)/Теория инф(лаб)\nКомп СС(пр/лб)\nКомп СС(лек)')
		elif message.text == 'Пятница':
			bot.send_message(message.chat.id, 'ООТПСП (лаб)\nВеб-тех (лек)\nТРПО(лаб/лек)')
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

# RUN
bot.polling(none_stop=True)