#!/usr/bin/env python3
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

from herucode import HeruLang


@app.route('/')
def hello_world():
    return """Endpoint for Herucode Parser"""


@app.route('/parse_post', methods=['POST'])
def parse_heru_post_arg():
    word_list = request.values.get('text', "")
    hl = HeruLang()
    return jsonify(hl.analyze(word_list))


@app.route('/parse', methods=['POST'])
def parse_heru_post_json():
    if request.is_json:
        words = request.json['text']
    else:
        words = ""
    hl = HeruLang()
    return jsonify(hl.analyze(words))


if __name__ == '__main__':
    app.run()

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)