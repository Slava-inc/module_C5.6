import telebot
from config import TOKEN
import requests
from extensions import ExchangeRate

with open('config.txt', 'r') as f:
    data = f.read().splitlines()
EXCH = data[0]
TOKEN = data[1] 
    
    

print(ExchangeRate.rate('USD', 'RUB'))


# bot = telebot.TeleBot(TOKEN)
# bot.polling(none_stop=True) #run bot, don't stop error appearing

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

