from lxml import html
import requests
from pprint import pprint


url = 'https://hanty.pulscen.ru/firms/070401-kabel-silovoj'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/104.0.0.0 Safari/537.36'}

responce = requests.get(url, headers=headers)

dom = html.fromstring(responce.text)

items = dom.xpath('//div[@class="ccd-content"]')
pprint(len(items))

list_items = []
for item in items:
    item_info = {}
    title = item.xpath('.//div/a[contains(@class, "ccd-title js-bp-title js-ykr-action js-ga-link")]/text()')

    item_info['title'] = title
    list_items.append(item_info)

pprint(list_items)


