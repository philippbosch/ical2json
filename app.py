#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, abort, jsonify, request
from icalendar import Calendar
from urllib import urlopen

app = Flask(__name__)

@app.route('/')
def index():
    return u'Please use like <code>http://<script>document.write(location.host);</script><noscript>ical2json.pb.io</noscript>/http://www.myserver.com/path/to/file.ics</code><br>Source code and instructions at <a href="http://github.com/philippbosch/ical2json">http://github.com/philippbosch/ical2json</a>.'

@app.route('/<path:url>')
def convert_from_url(url):
    if url == 'favicon.ico':
        abort(404)
    if not url.startswith('http'):
        url = 'http://%s' % url
    uh = urlopen(url)
    if uh.getcode() != 200:
        abort(404)
    ics = uh.read()
    uh.close()
    cal = Calendar.from_string(ics)
    data = {}
    data[cal.name] = dict(cal.items())

    for component in cal.subcomponents:
        if not data[cal.name].has_key(component.name):
            data[cal.name][component.name] = []

        comp_obj = {}
        for item in component.items():
            comp_obj[item[0]] = unicode(item[1])

        data[cal.name][component.name].append(comp_obj)

    resp = jsonify(data)
    if 'callback' in request.args:
        resp.data = "%s(%s);" % (request.args['callback'], resp.data)
    return resp

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
