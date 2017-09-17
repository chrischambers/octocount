#!/usr/bin/env python
# encoding: utf-8

from os.path import abspath, dirname, join
from tornado import web, wsgi
from tornado.httpclient import HTTPClient, HTTPError
from utils import extract_visible_words
from word_count import word_count
from wsgiref.simple_server import make_server

project_directory = abspath(dirname(__file__))


class Index(web.RequestHandler):

    def get(self):
        client = HTTPClient()
        context = {"url": "", "response": ""}
        url = self.get_query_argument("url", None)
        if url:
            try:
                response = client.fetch(url)
                context["url"] = url
                context['response'] = word_count(" ".join(
                    extract_visible_words(response)
                ))
            except HTTPError as e:
                pass
        self.render("index.html", **context)


settings = {
    "template_path": join(project_directory, "templates"),
    "static_path": join(project_directory, "static"),
    "debug": True,
}

app = web.Application([
    (r'/', Index),
], **settings)

application = wsgi.WSGIAdapter(app)

if __name__ == '__main__':
    with make_server('', 8888, application) as server:
        server.serve_forever()
