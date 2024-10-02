#from subprocess import check_output
import telebot;
bot = telebot.TeleBot('8051689493:AAGQB6Ec2DaFYh8JZsosDwvOjTKSoiWcW00'); #тут токен бота
@bot.message_handler(content_types=['text']) #слушаем бота
def get_text(message):
    if message.text == "Привет": #проверям сообщение от пользователя
        bot.send_message(message.from_user.id, "Здравствуй, мой дорогой друг!") #отвечаем пользователю
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "напиши: Привет")
    else:
        bot.send_message(message.from_user.id, "я тебя не понимаю, напиши '/help'")
bot.polling(none_stop=True, interval=0)# бот постоянно будет опрашивает сервера