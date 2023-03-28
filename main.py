from bs4 import BeautifulSoup
import requests


# server site rendering
def parse_ssr():
    response = requests.get('https://ru.investing.com/currencies/usd-rub')
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('span', {'class': 'text-2xl'}).text
    return data


print(parse_ssr())
