import requests
import time
import datetime

url_api_conversor = 'https://economia.awesomeapi.com.br/last/USD-BRL'

#get from public API in real time
def get_cotacao():
    response = requests.get(url_api_conversor)
    data = response.json()
    cotacao = float(data['USDBRL'].get('bid'))
    return cotacao

def rodar():
    while True:
        cotacao = get_cotacao()
        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%y %H:%M:%S")
        print(f'{date_time} -=- Cotação: R${cotacao:.4f}')
        time.sleep(1)

if __name__ == '__main__':
    rodar()