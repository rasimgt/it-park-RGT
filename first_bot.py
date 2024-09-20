import telebot;
bot = telebot.TeleBot('7935685520:AAGE8Ov2jk4vakLFHGE20YL3W-uAZ2xrn88'); #тут токен бота
@bot.message_handler(content_types=['text']) #слушаем бота
def get_text(message):
    if message.text == "Привет": #проверям сообщение от пользователя
        bot.send_message(message.from_user.id, "Здравствуй, мой дорогой друг!") #отвечаем пользователю
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "напиши: Привет")
    else:
        bot.send_message(message.from_user.id, "я тебя не понимаю, напиши '/help'")
bot.polling(none_stop=True, interval=0)# бот постоянно будет опрашивает сервер
