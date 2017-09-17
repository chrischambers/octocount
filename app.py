#!/usr/bin/env python
# encoding: utf-8

from tornado import web
from tornado.ioloop import IOLoop


class Index(web.RequestHandler):
    def get(self):
        self.write("Hello World!")


if __name__ == '__main__':
    app = web.Application([
        (r'/', Index),
    ])
    app.listen(8888)
    IOLoop.current().start()
