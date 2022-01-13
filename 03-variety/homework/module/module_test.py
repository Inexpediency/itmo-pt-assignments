import sys
import pytest
from pytest import mark

# noinspection PyPackages
from .module import do_something_stupid as dss1
# noinspection PyPackages
from ..module.module import do_something_stupid as dss2
from .module import do_fail


# @formatter:off
def do_nothing():
    return None
from homework.module.module import do_nothing as do_nothing1
# @formatter:on


def do_another_fail():
    raise ValueError()


def test_something_stupid():
    dss1()
    dss2()


# noinspection PyBroadException
@mark.parametrize('data', [
    [lambda: do_another_fail(), ValueError],
    [lambda: do_fail(10), ValueError],
    [lambda: do_fail(), NotImplementedError]
])
def test_fail(data):
    try:
        data[0]()
        pytest.fail('Expected failing raise')
    except Exception as e:
        print(e)
        if not isinstance(e, data[1]):
            pytest.fail('Wrong exception class')


def test_nothing():
    f = open(sys.modules[__name__].__file__).readlines()
    assert any([
        'module' in s and
        'do_nothing' in s and
        'import' in s and
        not s.strip().startswith('#') for s in f
    ])
    res = do_nothing()
    if res == 'nothing':
        pytest.fail('Function do_nothing from module overrides the local one')
    assert res is None
