#!/usr/bin/env python

def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    url = 'http://%s' % env['PATH_INFO'][1:]
    if env.has_key('QUERY_STRING') and len(env['QUERY_STRING']):
        url += "?%s" % (env['QUERY_STRING'])
    return [url + "\n"]
