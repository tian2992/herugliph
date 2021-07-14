#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

from herucode import HeruLang

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/parse_post', methods=['POST'])
def parse_heru_post_arg():
    words = []  # TODO: load words as post arg value
    hl = HeruLang(words)
    return {}


@app.route('/parse', methods=['POST'])
def parse_heru_post_json():
    words = []  # TODO: load words as json arg value
    hl = HeruLang(words)
    return {}


if __name__ == '__main__':
    app.run()
