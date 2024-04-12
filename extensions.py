import requests
from config import EXCH, keys

class ExchangeRate():
  @staticmethod
  def rate(*args):
    data = args[0]
    try:
      base = keys[data[0]]
    except KeyError:
      APIExeption(f'Неверно указана базовая валюта {data[0]}')
      return  

    try:
      quote = keys[data[1]]
    except KeyError:
      APIExeption(f'Неверно указана расчетная валюта {data[1]}')
      return 
    
    try:
      amount = float(data[2])
    except ValueError:
      APIExeption(f'Неверное значение количества {data[2]}')
      return
    
    if base == quote:
      raise APIExeption(f'Невозможно конвертировать одинаковые валюты {base}')    
      return
    
    print('Успешно конвертировано!')  
      
    url = 'https://v6.exchangerate-api.com/v6/'+ EXCH + '/latest/' + base
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates'][quote] * amount
  
class APIExeption(Exception):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)
    print(args[0])
    
if __name__ == '__main__':
  while True:
    query = input('Введите запрос на конвертацию: ')    
    values = query.split(' ')
    if values[0] == 'quit':
      break
    if len(values) != 3:
      try:
        raise APIExeption('Количество параметров при конвертации должно быть 3')
      except:
        continue

    ExchangeRate.rate(values)