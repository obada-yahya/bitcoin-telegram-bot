import requests
import time
api_key = "YOUR API KEY IN COINMARKETCAP "
bot_key = "YOUR BOT API IN THE TELEGRAM"
chat_id = "YOUR CHAT ID IN THE TELEGRAM"
time_interval = 60
num_of_requests = 10


def get_bitcoin_price():
    parameters = {
      'start': '1',
      'limit': '2',
      'convert': 'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': api_key,
    }
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    response = requests.get(url, params=parameters, headers=headers)
    response.raise_for_status()
    return response.json()


def send_message(price):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": f"the price of bitcoin is {price}",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()


while num_of_requests >= 1:
    data = get_bitcoin_price()["data"][0]["quote"]["USD"]["price"]
    send_message(data)
    time.sleep(time_interval)
    num_of_requests -= 1
