import requests
from lxml import html


def wikipedia(name):
    response = requests.get(f'https://ru.wikipedia.org/wiki/{name}')
    tree = html.fromstring(response.text)

    return tree.xpath("//p/b")[0].text
