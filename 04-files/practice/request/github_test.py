import pathlib

from github import github


def test_github():
    loc = pathlib.Path('.').absolute()
    while not loc.name.startswith('assignment-04-files'):
        loc = loc.parent
    assert loc.name.split('-', 3)[-1] == github()
