
import telebot
from telebot import types

"""
Калькулятор
1. создать 4 переменные:
первое число, операция, второе число результата
2. Создать функцию, которая делает вычисления, 
3.запросить у пользователя первое число, операцию, второе число
4 сделать вычисления, в зависимост от выбора пользователя, показать результата, или продолжить вычисления.
5. опретор + приходит строкой, он не во что не преобразовывается. ведь это опратор, т.е. 3 "+" 2 - ошибка. 
используется функция eval(), в которую передаем строку "3+2" и операвция выполняется верно.
6. зациклить вычисления, т.е. если выбрал результат - показать результат, 
если "продолжить вычисления" - передать результат вычисления как первое число.

"""
bot = telebot.TeleBot("5465709277:AAEAF06f3GE2L24Y-jI0KuaT_Q5Kwo693j4")

user_num1 = ''
user_num2 = ''
user_proc = '' # оператор 
user_result = None


# если /start, /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # убрать клавиатуру Telegram полностью - reply_markup = markup
    markup = types.ReplyKeyboardRemove(selective=False)

    msg = bot.send_message(message.chat.id, "Привет! "  + message.from_user.first_name + ", я бот-калькулятор\nВведите число", reply_markup = markup)
    bot.register_next_step_handler(msg, process_num1_step)

# введите первое число
def process_num1_step(message, user_result = None):
    try:
        global user_num1
        user_num1 = int(message.text)
        # запоминаем число
        # #если только начали /start
        if user_result == None:
            user_num1 = int(message.text)
 
        else:
            # ecли был передан результат ранее
            # пишем в первое число не спрашивая
            user_num1 = str(user_result)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembtn1 = types.KeyboardButton('+')
        itembtn2 = types.KeyboardButton('-')
        itembtn3 = types.KeyboardButton('*')
        itembtn4 = types.KeyboardButton('/')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

        msg = bot.send_message(message.chat.id, 'Выберите операцию', reply_markup = markup)
        bot.register_next_step_handler(msg, process_proc_step)
    except Exception as e:
        bot.reply_to(message, 'Это не число, или что-то пошло не так...')

# выберите операцию +, -, *, /
def process_proc_step(message):
    try:
        global user_proc
        # запоминаем операцию
        user_proc = message.text
        # убрать клавиатуру телеграм полностью
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(message.chat.id, 'Введите еще число', reply_markup = markup)
        bot.register_next_step_handler(msg, process_num2_step)
    except Exception as e:
         bot.reply_to(message, 'Это не число! Или что-то пошло не так...')
        
# второе число

def process_num2_step(message):
    try:
        global user_num2
        # запоминаем число
        user_num2 = int(message.text)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembtn1 = types.KeyboardButton('Результат')
        itembtn2 = types.KeyboardButton('Продолжить вычисления')
        markup.add(itembtn1, itembtn2)

        msg = bot.send_message(message.chat.id, 'Показать результат или продолжить операцию?', reply_markup = markup)
        bot.register_next_step_handler(msg, process_alternative_step)
    except Exception as e:
        bot.reply_to(message, 'Это не число... или что-то пошло не так...')


# показать результат или продолжить операцию

def process_alternative_step(message):
    try:
        # делать вычисления
        calc()
        # убрать клавиатуру телеграм полностью
        markup = types.ReplyKeyboardRemove(selective=False)

        if message.text.lower() == 'результат':
            bot.send_message(message.chat.id, calcResultPrint(), reply_markup = markup)
        elif message.text.lower() == 'продолжить вычисления':
            # перейти на шаг, где спрашиваем оператор
            # передаем ркзультат как первое число
            process_num1_step(message, user_result)

    except Exception as e:
        bot.reply_to(message, 'что-то пошло не так...')

#вывод результата пользователю


def calcResultPrint():
    global user_num1, user_num2, user_proc, user_result
    return "Результат: " + str(user_num1) + '' + user_proc + '' + str(user_num2) + '=' + str(user_result)


# вычисления 

def calc():
    global user_num1, user_num2, user_proc, user_result

    user_result = eval(str(user_num1) + user_proc + str(user_num2))

    return user_result

bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)

#bot.polling(none_stop=True, interval=0) # запуск бота на постоянной основе

