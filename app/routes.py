from app import app
from datetime import datetime
from flask import  make_response, request
from flask.json import  jsonify

from .services import massegeSender


@app.route('/')
def index():
    return "Hi, fellow Flask developer!"

@app.route('/sendMessage', methods=['POST'])
def send_message():
    data = request.json
    return make_response(jsonify(result=massegeSender(data)), 200)
