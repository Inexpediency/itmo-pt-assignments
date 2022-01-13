from __future__ import annotations
from homework.module.module_helper import do_another_fail


def do_something_stupid():
    pass


def do_fail(value: None | int = None):
    if value is None:
        raise NotImplementedError()
    do_another_fail()


def do_nothing():
    return 'nothing'
