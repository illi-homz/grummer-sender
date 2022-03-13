from cmath import log
import requests
import json
from flask import jsonify
import os
from base64 import b64encode

botToken = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
url = f'https://api.telegram.org/bot{botToken}/sendMessage'
url_photo = f'https://api.telegram.org/bot{botToken}/sendPhoto'
url_media_group = f'https://api.telegram.org/bot{botToken}/sendMediaGroup'


def data(msg):
    return {'chat_id': chat_id, 'text': msg, 'parse_mode': 'markdown'}


def massegeSender(msg):
    r = requests.post(url, data(msg))
    return r.ok


def photoSender(photo):
    params = {'chat_id': chat_id}
    files = {'photo': photo}
    r = requests.post(url_photo, params, files=files)
    print('photoSender', r.json())
    return r.ok


def mediaGroupSender(files):
    params = {
        'chat_id': chat_id,
        'media': [{'type': 'photo', 'media': f'attach://{file.filename}'} for file in files]
    }

    params['media'] = json.dumps(params['media'])

    current_files = {}
    for file in files:
        current_files[file.filename] = file

    r = requests.post(url_media_group, params, files=current_files)
    print('mediaGroupSender', r.json())
    return r.ok
