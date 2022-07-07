from requests import Request , Session

import os.path
from os import path

import json
import pprint

import ctypes  # An included library with Python install.

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

import pickle

APIkey = ''
filename = 'myAPIkey.pk'

file = open(filename,'a+')
file.close

# load APIkey
with open(filename, 'r') as fi:
    APIkey = fi.read()

if not APIkey:
    APIkey = input("Please insert your coinmarketcap API KEY: ")

with open(filename, 'w') as f:
    f.write(APIkey)

##Mbox('Message', 'Check file!',0)

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'symbol':'BTC,ETH',
    'convert':'USD'
}

headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':APIkey##'84b475f2-b479-42f2-bab6-2407d46bd845'
}


session = Session()
session.headers.update(headers)

##print(APIkey)
##Mbox('Message', 'Make sure you´re using your own coinmarketcap API KEY!',0)

response = session.get(url, params=parameters)
pprint.pprint(json.loads(response.text)['data']['BTC']['quote']['USD']['price'])
