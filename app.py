#!/usr/bin/env python
# encoding: utf-8

from os.path import abspath, dirname, join
from tornado import web, wsgi
from tornado.httpclient import HTTPClient, HTTPError
from utils import extract_visible_words
from word_count import word_count
from word_cloud import word_cloud
from wsgiref.simple_server import make_server
import validators

project_directory = abspath(dirname(__file__))


class Index(web.RequestHandler):

    def get(self):
        client = HTTPClient()
        context = {"url": "", "word_cloud": "", "error": ""}
        url = self.get_query_argument("url", None)
        if not validators.url(url):
            context['error'] = "'{}' is an invalid URL!".format(url)
        else:
            try:
                response = client.fetch(url)
                context["url"] = url
                context['word_cloud'] = word_cloud(word_count(
                    extract_visible_words(response)))
            except HTTPError as e:
                context['error'] = "I cannot access that URL"
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
