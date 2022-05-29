import telebot

bot = telebot.TeleBot('5198683969:AAF_PzZ82SizhqndIrhKv6gDCIQzXgyBklc') # привязка к боту

# отслеживание команд
@bot.message_handler(commands_types=['text'])
def start(message):
    #bot.send_message(message.chat.id, 'Привет')#'<b>Hello</b>', parse_mode='html')
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.") 

bot.polling(none_stop=True, interval=0)
