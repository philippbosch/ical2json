#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/<path:url>')
def index(url):
    url = 'http://%s' % url
    return url

if __name__ == '__main__':
    app.run(debug=True)
