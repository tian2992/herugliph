#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

from herucode import HeruLang


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/parse_post', methods=['POST'])
def parse_heru_post_arg():
    word_list = request.values.get('text', "")
    hl = HeruLang()
    return hl.analyze(word_list)


@app.route('/parse', methods=['POST'])
def parse_heru_post_json():
    if request.is_json:
        words = request.json['text']
    else:
        words = ""
    hl = HeruLang()
    return hl.analyze(words)


if __name__ == '__main__':
    app.run()
