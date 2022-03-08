import requests
import os

botToken = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
url = f'https://api.telegram.org/bot{botToken}/sendMessage'
url_photo = f'https://api.telegram.org/bot{botToken}/sendPhoto'

def data(msg):
    return {'chat_id': chat_id,'text': msg,'parse_mode': 'markdown'}


def massegeSender(msg):
    r = requests.post(url, data(msg))
    return r.ok

def photoSender(photo):
    params = {'chat_id': chat_id}
    files = {'photo': photo}
    r = requests.post(url_photo, params, files=files)
    return r.ok
