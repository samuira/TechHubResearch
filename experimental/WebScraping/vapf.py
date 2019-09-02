# from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import requests
import xmltodict
from geopy.geocoders import Nominatim
import os
from tqdm import tqdm


# chrome driver
# driver = webdriver.Chrome()

# firefox driver
# driver = webdriver.Firefox()

# driver.get('https://net.vapf.com/oferta-inmobiliaria.xml?lang=en&CodigoVendedor=16475&CodigoRepresentante=EUESA00-KARAKIR')
# content = driver.page_source
# soup = BeautifulSoup(content, "xml")
# expected_key_set = ['ref', 'price', 'price_freq', 'type', 'address', 'lat', 'long', 'beds', 'baths', 'pools',
#                         'built', 'plot', 'desc', 'features', 'images']
# for a in soup.findAll('property'):
#     print(a.ref.string)
#     print(a)
#     break

site = requests.get('https://net.vapf.com/oferta-inmobiliaria.xml?lang=en&CodigoVendedor=16475&CodigoRepresentante=EUESA00-KARAKIR')

dict_items = xmltodict.parse(site.text)['properties']['property']

lis = list()
with tqdm(total=len(dict_items)) as pbar:
    for item in tqdm(dict_items):
        dic = dict()
        dic['ref'] = item.get('ref', '')
        dic['price'] = item['price']['#text'].split(',')[0].replace('.','')
        dic['price_freq'] = 'New Build' if next(filter(lambda x: 'new_home' in x.get('@type'), item['features']['feature'])).get('#text') == 'SI' else ''
        dic['type'] = item.get('type', '')
        dic['address'] = item.get('town', '')
        dic['lat'] = item['location'].get('latitude', '') if item.get('location') else ''
        dic['long'] = item['location'].get('longitude', '') if item.get('location') else ''
        dic['beds'] = item.get('beds', '')
        dic['baths'] = item.get('baths', '')
        dic['pools'] = 1 if next(filter(lambda x: 'pool' in x.get('@type'), item['features']['feature'])).get('#text') == 'SI' else 0
        dic['built'] = item['surfaces']['total']['#text'] if item.get('surfaces') else ''
        dic['plot'] = item['surfaces']['plot']['#text'] if item.get('surfaces') else ''
        dic['desc'] = item['desc']['en'].replace(',', ';')
        dic['features'] = ';'.join([feature.get('@type') for feature in filter(lambda x: 'SI' in x.get('#text'), item['features']['feature'])])
        dic['images'] = ';'.join(item['photogallery']['picture'])
        lis.append(dic)
        pbar.update(1)


xml_table = pd.read_json(json.dumps(lis))
xml_table.to_csv('vapf.csv', index=False)
