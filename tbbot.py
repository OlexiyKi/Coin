import telebot
import secretkey


bot = telebot.TeleBot(secretkey.token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "This bot will warn you a downtrend")



@bot.message_handler()
def send_warn(message):
    bot.reply_to(message, 'attention! ')


bot.infinity_polling()