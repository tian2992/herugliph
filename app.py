#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

from herucode import HeruLang

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
