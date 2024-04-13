keys = {
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB',        
}

with open('config.txt', 'r') as f:
    data = f.read().splitlines()
EXCH = data[0].replace('EXCH = ', '')
TOKEN = data[1].replace('TOKEN = ', '')