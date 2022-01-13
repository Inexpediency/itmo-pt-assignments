def save_color(color, filename):
    """Сохранить цвет в файл в формате JSON (см. _legend.md)"""
    import json

    with open(filename, 'w+', encoding='utf-8') as file:
        json.dump(color, file)


def load_color(filename):
    """Вернуть цвет, записанный в JSON-файле"""
    import json

    with open(filename, 'r+', encoding='utf-8') as file:
        return json.load(file)


def links(filename):
    """Вывести все страницы из JSON-структуры и подсчитать количество ссылок на каждую. (см. legend)"""
    import json

    websites, table = dict(), dict()
    with open(filename, 'r+', encoding='utf-8') as file:
        websites = json.load(file)['websites']

    for website in websites:
        url, links = website['url'], website['links']

        if url not in table:
            table[url] = 0

        for link in links:
            if link not in table:
                table[link] = 1
            else:
                table[link] += 1

    return table.items()
