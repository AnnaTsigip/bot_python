import telebot

bot = telebot.TeleBot('5516399527:AAH9kSUyOOzRtUP0QMhxosNp0yV6xG9UqNA') # привязка к боту

# # функция удаления
# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Давай поиграем?')

# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     if message.text == "давай" or message.text == "ok":
#         bot.send_message(message.from_user.id, 'Сколько будет конфет: ')
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

candies = 0
take = 0

# def get_candies(message):
#     global candies
#     candies = message.text
#     bot.send_message('Сколько будет конфет:?')
#     bot.register_next_step_handler(message, get_age)

def get_candies(message):
    global candies;
    while candies == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
      bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'

# candies = int(input('Сколько конфет: '))
# take = int(input("Максимальное количество конфет можно взять: "))

# Получение сообщений от пользователя
# @bot.message_handler(content_types=int(input(" ")))
# def handle_text(message):
#     bot.send_message(message.chat.id, take_to_have_for_first(candies, take):
# (message.text))

bot.polling(none_stop=True, interval=0) # запуск бота на постоянной основе





# candies = int(input('Сколько конфет: '))
# take = int(input("Максимальное количество конфет можно взять: "))
# # сколько нужно взять конфет для победы: 
def take_to_have_for_first(candies, take):
     take_candies = candies % (take + 1)
     if take_candies == 0:
         take_candies = take
     return take_candies


# count = 0
# while candies > 0:
#     count += 1
#     player = int(input("Ход первого игрока. Возьмите конфеты: "))
#     candies = candies - player
#     if candies > 0:
#         bot = take_to_have_for_first(candies, take)
#         print(f'bot взял {bot} конфет')
#         candies = candies - int(bot)
#         print(f'осталось конфет: {candies}')
#         #print(take_to_have_for_first(candies, take))
# if candies == 0:
#     print('Игра окончена')
# if count % 2 == 0:
#     print(f'Победил игрок player')
# else:
#     print(f'Победил игрок bot')