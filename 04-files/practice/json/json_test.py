from collections import Counter

import pytest
import os
import practice.json.json as json


color_data = [
    ('output.json', {'r': 255, 'g': 0, 'b': 0, 'a': 0.5}, '{"r": 255, "g": 0, "b": 0, "a": 0.5}'),
    ('output.json', {'r': 0, 'g': 0, 'b': 0, 'a': 1.}, '{"r": 0, "g": 0, "b": 0, "a": 1.0}'),
    ('output.json', {'r': 200, 'g': 100, 'b': 255, 'a': 0.}, '{"r": 200, "g": 100, "b": 255, "a": 0.0}'),
    ('output.json', {'r': 0, 'g': 1, 'b': 11, 'a': 0.1}, '{"r": 0, "g": 1, "b": 11, "a": 0.1}'),
]


@pytest.mark.parametrize('data', color_data)
def test_save_color(data):
    # noinspection PyArgumentList
    try:
        json.save_color(data[1], data[0])
        with open(data[0], 'r') as file:
            assert file.read() == data[2]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0]):
            os.remove(data[0])


@pytest.mark.parametrize('data', color_data)
def test_load_color(data):
    # noinspection PyArgumentList
    try:
        with open(data[0], 'w') as file:
            file.write(data[2])
        assert json.load_color(data[0]) == data[1]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0]):
            os.remove(data[0])


websites_file = 'websites.json'
websites_json = """{
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
"""

links_expected = [
    ('google.com', 1),
    ('google.com/search', 0),
    ('google.com/search/2', 1),
    ('microsoft.com', 2),
    ('aliexpress.com', 1),
    ('twitter.com', 0),
    ('facebook.com/post/1271', 1),
    ('facebook.com/post/3411', 1)
]


def test_links():
    try:
        with open(websites_file, 'w') as file:
            file.write(websites_json)
        assert Counter(json.links(websites_file)) == Counter(links_expected)
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(websites_file):
            os.remove(websites_file)
