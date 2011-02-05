#!/usr/bin/env python

from flask import Flask, abort, jsonify, request
from icalendar import Calendar
from urllib import urlopen

app = Flask(__name__)

@app.route('/<path:url>')
def index(url):
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
    app.run(debug=True)
