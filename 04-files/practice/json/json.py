import json


def save_color(color, filename):
    """Сохранить цвет в файл в формате JSON (см. _legend.md)"""
    with open(filename, 'w') as f:
        json.dump(color, f)


def load_color(filename):
    """Вернуть цвет, записанный в JSON-файле"""
    with open(filename, 'r') as f:
        return json.load(f)


def links(filename):
    """Вывести все страницы из JSON-структуры и подсчитать количество ссылок на каждую. (см. legend)"""
    with open(filename, 'r') as f:
        data = dict(json.load(f))
    result = {}
    for site in data['websites']:
        site_url = site['url']
        if site_url not in result.keys():
            result[site_url] = 0

        site_links = site['links']
        for url in site_links:
            if url in result.keys():
                result[url] += 1
            else:
                result[url] = 1

    return [(k, v) for k, v in result.items()]
