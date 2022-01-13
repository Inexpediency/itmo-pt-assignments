import pytest
import bonus


transform_test_data = [
    (['hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]], 5),
    (['hit', 'cog', ["hot", "dot", "dog", "lot", "log"]], 0),
    # cat -> cad -> mad -> maw -> mow -> meow
    (['cat', 'meow', ["cad", "car", "card", "mad", "maw", "mow", "meow", "load", "loan", "ca", "meows"]], 6),
    # a -> aa -> aaa
    (['a', 'aaa', ['aa', 'ab', 'ac', 'acd', 'aca', 'aaa']], 3),
    (['a', 'aabb', ['aa', 'ab', 'ac', 'acd', 'aca', 'aaa', 'aabb']], 0),
    # itmo -> ittmo -> ittm -> itt -> it
    (['itmo', 'it', ['itt', 'ittmo', 'ittm', 'itt', 'it', 'it', 'i', 'i', 'ittmoo', 'itmoo', 'ifmo']], 5),
    # rar -> Rar -> RAr -> RAR
    (['rar', 'RAR', ['rat', 'rot', 'Rot', 'RAt', 'RAM', 'rar', 'Rar', 'RAr', 'RAR']], 4)
]


@pytest.mark.parametrize('data', transform_test_data)
def test_transform(data):
    # noinspection PyArgumentList
    assert bonus.transform(*data[0]) == data[1]
