#!/usr/bin/env python
# encoding: utf-8

from tornado import web, wsgi
from wsgiref.simple_server import make_server


class Index(web.RequestHandler):
    def get(self):
        self.write("Hello World!")


app = web.Application([
    (r'/', Index),
])
application = wsgi.WSGIAdapter(app)

if __name__ == '__main__':
    with make_server('', 8888, application) as server:
        server.serve_forever()
