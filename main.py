import telebot
import time

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello!')


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, '/start - Start\n/help - Help')


bot.infinity_polling()
