import telebot
from telebot import apihelper


Token = '1101589848:AAEfRJ_ML0fouwFYFnd1-NFcBQ6jv7JzeDs'

Bot_URL = f'https://api.telegram.org/bot{Token}'

proxies = {
    'http': 'http://88.199.21.76:80',
    'https': 'http://88.199.21.76:80'
}

apihelper.proxy = proxies
bot = telebot.TeleBot(Token)

@bot.message_handler(command = ['start'])
def command_answer(message):
    bot.reply_to(message, f'Рад Вас приветствовать,{message.from_user.username}!')

@bot.message_handler(command = ['help'])
def command_help(message):
    bot.reply_to(message, 'Обратитесь за помощью к администратору!')

@bot.message_handler(command = ['quit'])
def command_help(message):
    bot.reply_to(message, 'Хотите выйти? Примените формулу прощания!')

#инициация прощания
@bot.message_handler(content_types = ['text'])
def farewell(message):
    if message.text == 'До свидания!':
        bot.reply_to(message, f'До связи,{message.from_user.username}!')

#отсылка к команде "/help"
@bot.message_handler(content_types = ['text'])
def receive(message):
    if '?' in message.text:
        bot.reply_to(message, f'Вы написали: {text}. Если у вас вопрос, наберите команду /help')

#ответ на вопрос "Кто ты?"
@bot.message_handler(content_types=['text'])
def bot_horoscope(message):
    if message.text == 'Кто ты?':
        bot.reply_to(message, 'Я твой всезнающий мистер Бот, тебе повезло!')

bot.polling()

