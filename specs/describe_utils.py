from utils import get_response_charset


def describe_get_response_charset():
    def parses_out_the_charset_correctly(response):
        response.headers.add('Content-Type', "text/html; charset=ISO-8859-1")
        assert get_response_charset(response) == "ISO-8859-1"

    def defaults_to_utf8_if_no_charset_specified(response):
        response.headers.add('Content-Type', "text/html")
        assert get_response_charset(response) == "utf-8"
