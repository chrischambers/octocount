#!/usr/bin/env python
# encoding: utf-8

import cgi

from bs4 import BeautifulSoup
from os.path import abspath, dirname, join
from tornado import web, wsgi
from tornado.httpclient import HTTPClient, HTTPError
from word_count import word_count
from wsgiref.simple_server import make_server

project_directory = abspath(dirname(__file__))

import re


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True


def get_content_charset(response, default=None):
    content_type, params = cgi.parse_header(
        response.headers['Content-Type']
    )
    return params.get('charset', default)


class Index(web.RequestHandler):

    def get(self):
        client = HTTPClient()
        context = {"url": "", "response": ""}
        url = self.get_query_argument("url", None)
        if url:
            try:
                response = client.fetch(url)
                # text = response.body.decode(self.get_content_charset('utf-8'))
                text = response.body.decode(get_content_charset(response, 'utf-8'))
                soup = BeautifulSoup(text, "html.parser")
                context["url"] = url
                data = soup.findAll(text=True)
                context['response'] = word_count(" ".join(filter(visible, data)))
                # context["response"] = word_count(soup.get_text())
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
