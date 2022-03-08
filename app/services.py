import requests
import json
from flask import jsonify
import os

botToken = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
url = f'https://api.telegram.org/bot{botToken}/sendMessage'
url_photo = f'https://api.telegram.org/bot{botToken}/sendPhoto'

def data(msg):
    return {'chat_id': chat_id,'text': msg,'parse_mode': 'markdown'}

def photoData(photo):
    return {'chat_id': chat_id, 'photo': photo}


def massegeSender(msg):
    r = requests.post(url, data(msg))
    return r.ok

def photoSender(photo):
    r = requests.post(url_photo, photoData(photo))
    return r.ok
