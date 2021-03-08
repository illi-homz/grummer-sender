import requests
import json
from flask import jsonify
import os

botToken = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
url = 'https://api.telegram.org/bot{botToken}/sendMessage'.format(botToken=botToken)

def data(msg):
    return {'chat_id': chat_id,'text': msg,'parse_mode': 'markdown'}


def massegeSender(msg):
    r = requests.post(url, data(msg))
    return r.ok
