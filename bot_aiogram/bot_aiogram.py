#import telebot

from aiogram import Bot, Dispatcher, executor, types

from dotenv import load_dotenv
import os
load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['start'])
def send_start(message):
#    bot.send_message(message.from_user.id, 'Привет!')   #декоратор. после написания старт выходит сообщение привет
    if message.text == '\start':
        bot.send_message(message.from_user.id, 'Hello!')
    else:
        if message.text == '\help':
            bot.send_message(message.from_user.id, 'Это помощь')


@bot.message_handler(content_types=['text'])

#def get_message(message):
#    bot.send_message(message.from_user.id, message.text)  #просто ответ

def reply_text(message):
    bot.reply_to(message, message.text)    # бот отправляет ответное письмо



bot.polling(non_stop=True)