#!/usr/bin/env python
# encoding: utf-8

from os.path import abspath, dirname, join
from tornado import web, wsgi
from wsgiref.simple_server import make_server

project_directory = abspath(dirname(__file__))


class Index(web.RequestHandler):
    def get(self):
        self.render("index.html")


settings = {
    "template_path": join(project_directory, "templates"),
    "static_path": join(project_directory, "static"),
    # "debug": True,
}

app = web.Application([
    (r'/', Index),
], **settings)

application = wsgi.WSGIAdapter(app)

if __name__ == '__main__':
    with make_server('', 8888, application) as server:
        server.serve_forever()
