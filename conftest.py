import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.httputil import HTTPHeaders


@pytest.fixture
def response():
    request = HTTPRequest("http://example.com")
    headers = HTTPHeaders({"content-type": "text/html"})
    return HTTPResponse(request, 200, headers)
    return HTTPResponse(request, 200, {"content-type": "text/html\r\ncharset=ISO-8859-1"})
