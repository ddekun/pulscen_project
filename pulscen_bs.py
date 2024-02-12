from pprint import pprint
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


url = 'https://hanty.pulscen.ru/firms/070401-kabel-silovoj'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/104.0.0.0 Safari/537.36'}

responce = requests.get(url, headers=headers)

soup = bs(responce.text, 'html.parser')
print(soup)
names = soup.find_all('a', {'class': 'ccd-title js-bp-title js-ykr-action js-ga-link'})
print(names)
