import telebot as tg

from functions.badword_detector import badword_detector_function

with open('info/token.txt', encoding='utf8') as file:
    token = file.readline()
    bot = tg.TeleBot(token)
    file.close()

@bot.message_handler(commands=['start'], chat_types=['private'])
def start_function(message):
    bot.send_message(message.from_user.id, 'Бот для фильтрации матных слов! \nФильтр бота можно изменять \nRevoltTeam 2022')

@bot.message_handler(func= lambda message: True, chat_types=['group', 'supergroup'])
def badword_function(message):
    print(message.text, badword_detector_function(message.text))
    if badword_detector_function(message.text) == True:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, написал плохое слово! Оно было удалено')

bot.infinity_polling()
