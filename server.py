#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from wsgi import app

HTTP_HOST = "localhost"
HTTP_PORT = 8765

server = make_server(HTTP_HOST, HTTP_PORT, app)
print "Serving HTTP on %s:%s …" % (HTTP_HOST, HTTP_PORT)
server.serve_forever()
