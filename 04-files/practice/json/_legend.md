# Json

Для работы с форматом JSON в Python есть стандартный модуль `json`.
Подробнее о формате и работе с ним можно почитать, например,
[здесь](https://python-scripts.com/json).

Небольшой пример:
```python
import json

# Был какой-то объект...
x = {
    'message': 'hi!',
    'id': 259
}

# Получили JSON-строку, которую можем, например, вывести или записать в файл
json_str = json.dumps(x)

# По JSON-строке восстановили исходный объект
original_object = json.loads(json_str)
```

## `save_color`

Аргумент `color` - это `dict` с ключами `r`, `g`, `b` -
красный, зелёный и синий компонент соответственно (целые числа 0 - 255),
а также `a` - прозрачность (число с плавающей точкой от 0 до 1).

Необходимо записать переданный цвет в файл с именем `filename` в формате JSON,
используя стандартные средства Python.

Пример:
```python
color = {
    'r': 255,
    'g': 0,
    'b': 0,
    'a': 0.5
}
save_color(color, 'output.json')
```

Результат в output.json:
```json
{ "r": 255, "g": 0, "b": 0, "a": 0.5 }
```

## `load_color`
Аналогично предыдущему заданию, нужно загрузить цвет из указанного JSON-файла
и вернуть в виде `dict` описанной ранее структуры.

## `links`
В указанном JSON-файле хранится структура, представляющая
некоторое подмножество веб-страниц со списком исходящих ссылок на другие страницы:


```json
{
  "websites": [
    {
      "url": "google.com/search",
      "links": [
        "microsoft.com",
        "aliexpress.com",
        "google.com/search/2"
      ]
    },
    {
      "url": "microsoft.com",
      "links": []
    },
    {
      "url": "twitter.com",
      "links": [
        "google.com",
        "facebook.com/post/1271",
        "facebook.com/post/3411",
        "microsoft.com"
      ]
    }
  ]
}
```

Реализованная функция должна вернуть список всех страниц
с количеством ссылок на каждую из них.

Пример результата для приведённого выше файла:
```python
[
    ('google.com', 1),
    ('google.com/search', 0),
    ('google.com/search/2', 1),
    ('microsoft.com', 2),
    ('aliexpress.com', 1),
    ('twitter.com', 0),
    ('facebook.com/post/1271', 1),
    ('facebook.com/post/3411', 1)
]
```

Порядок записей в возвращаемом списке не важен.
