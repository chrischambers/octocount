from bs4 import BeautifulSoup
import cgi
import re


def visible_elements(element):
    technical_details = ['style', 'link', 'script', '[document]', 'head', 'title']
    if element.parent.name in technical_details:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True


def get_response_charset(response, default='utf-8'):
    content_type, params = cgi.parse_header(
        response.headers['Content-Type']
    )
    return params.get('charset', default)


def response_to_text(response):
    return response.body.decode(get_response_charset(response))


def extract_visible_words(response):
    text = response_to_text(response)
    soup = BeautifulSoup(text, "html.parser")
    data = soup.findAll(text=True)
    return filter(visible_elements, data)


def normalize(lower_bound, upper_bound, dataset):
    """
    Normalises values in dataset from lower_bound to upper_bound.
    """
    maximum, minimum = max(dataset), min(dataset)
    diff = maximum - minimum
    bounds = upper_bound - lower_bound

    def f(x):
        return (bounds * (x - minimum) / diff) + lower_bound
    return map(f, dataset)
