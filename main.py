import telebot
import time

# Create bot
bot = telebot.TeleBot('')

# Create blacklist
blacklist = ['криптовалюте']


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет!\n Для получения справки воспользуйся командой /help.')


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, '/start - Старт\n/help - Помощь\n/kick - Исключить участника')


@bot.message_handler(commands=['kick'])
def kick(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'creator' or user_status == 'administrator':
            bot.reply_to(message, 'Невозможно исключить администартора.')
        else:
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, f'Участник {message.reply_to_message.from_user.username} был исключен.')
    else:
        bot.reply_to(message, 'Используйте эту команду в ответ на сообщение участника, которого нужно исключить.')


@bot.message_handler()
def handle_message(message):
    if check_message(message):
        bot.reply_to(message, 'У нас так не принято.')
    else:
        print(message.text)


def check_message(message):
    for word in blacklist:
        if word in message.text.lower():
            return True
    return False


bot.infinity_polling()
