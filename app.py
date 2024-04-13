import telebot
from config import TOKEN
from extensions import ExchangeRate
    
    
print(ExchangeRate.rate(['доллар', 'рубль', 1]))


# bot = telebot.TeleBot(TOKEN)
# bot.polling(none_stop=True) #run bot, don't stop error appearing

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

