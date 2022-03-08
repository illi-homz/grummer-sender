from cmath import log
from app import app
from flask import  make_response, request
from flask.json import  jsonify

from .services import massegeSender, photoSender, mediaGroupSender


@app.route('/')
def index():
    return "Hi, fellow Flask developer!"

@app.route('/sendMessage', methods=['POST'])
def send_message():
    data = request.json
    return make_response(jsonify(result=massegeSender(data)), 200)

@app.route('/sendPhoto', methods=['POST'])
def send_photo():
    data = request.get_data()
    return make_response(jsonify(result=photoSender(data)), 200)

@app.route('/sendPhotos', methods=['POST'])
def send_photos():
    print()
    files = request.files.getlist('files')
    return make_response(jsonify(result=mediaGroupSender(files)), 200)
