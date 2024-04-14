import telebot
from config import TOKEN, keys
from extensions import ExchangeRate, APIExeption
    
    
# print(ExchangeRate.rate(['доллар', 'рубль', 1]))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	txt = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>'
	bot.reply_to(message, txt)

@bot.message_handler(commands=['values'])
def values(message):
	txt = 'Доступные валюты:'
	for key in keys:
		txt = '\n'.join((txt, key, ))
	bot.reply_to(message, txt)

@bot.message_handler(content_types=['text',])
def convert(message):
	try:
		values = message.text.split(' ')
		if len(values) != 3:
			raise APIExeption('Количество параметров при конвертации должно быть 3')
		result = ExchangeRate.get_price(values)
	except APIExeption as e:
		bot.send_message(message.chat.id, f'Ошибка пользователя\n{e}')
	except Exception as e:
		bot.reply_to(message, f'Не удалось обработать команду\n{e}')
	else:
		bot.send_message(message.chat.id, result)

bot.polling() #run bot, don't stop error appearing none_stop=True