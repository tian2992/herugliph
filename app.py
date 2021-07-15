#!/usr/bin/env python3
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

from herucode import HeruLang


@app.route('/')
def hello_world():
    return ""


@app.route('/parse_post', methods=['POST'])
def parse_heru_post_arg():
    app.logger.info("Parsing post argument")
    word_list = request.values.get('text', "")
    hl = HeruLang()
    return jsonify(hl.analyze(word_list))


@app.route('/parse', methods=['POST'])
def parse_heru_post_json():
    app.logger.info("Parsing as json argument")
    if request.is_json:
        try:
            words = request.json['text']
        except KeyError:
            app.logger.error("No text value on JSON")
            return {}
    else:
        app.logger.error("Invalid JSON value posted")
        words = ""
    hl = HeruLang()
    return jsonify(hl.analyze(words))


if __name__ == '__main__':
    import os
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)