import requests
from config import EXCH, keys

class ExchangeRate():
  @staticmethod
  def get_price(*args):
    data = args[0]
    try:
      base = keys[data[0]]
    except KeyError:
      raise APIExeption(f'Неверно указана базовая валюта {data[0]}')

    try:
      quote = keys[data[1]]
    except KeyError:
      raise APIExeption(f'Неверно указана расчетная валюта {data[1]}')
    
    try:
      amount = float(data[2])
    except ValueError:
      raise APIExeption(f'Неверное значение количества {data[2]}')
    
    if base == quote:
        raise APIExeption(f'Невозможно конвертировать одинаковые валюты {data[0]}')  
    
    # print('Успешно конвертировано!')  
      
    url = 'https://v6.exchangerate-api.com/v6/'+ EXCH + '/latest/' + base
    response = requests.get(url)
    conv = response.json()
    result = conv['conversion_rates'][quote] * amount
    
    return f'цена {amount} {data[0]} в {data[1]} - {result}'
  
class APIExeption(Exception):
  pass

