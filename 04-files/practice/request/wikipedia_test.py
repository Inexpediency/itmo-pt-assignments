import pathlib
from pytest import mark

from wikipedia import wikipedia


@mark.parametrize('name, title', [
    ('Python', 'Python'),
    ('ICPC', 'Международная студенческая олимпиада по программированию'),
    ('Страусятина', 'Мя́со стра́уса (страуся́тина)'),
    ('RAM', 'Запоминающее устройство с произвольным доступом'),
    ('No Game No Life', 'Нет игры жизни нет'),
])
def test_wikipedia(name, title):
    assert wikipedia(name) == title
