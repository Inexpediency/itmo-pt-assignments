import pytest
import os
import table_of_contents


test_data = [
    (
        'abc.txt',
        '#aaaa\nbbbb\n#cccc\ndddd',
        '6\n#aaaa\nbbbb\n#cccc\ndddd\n1.....aaaa\n3.....cccc'
    ),
    (
        'abc.txt',
        'aaaa\nbbbb\ncccc\ndddd',
        '6\naaaa\nbbbb\ncccc\ndddd\n'
    ),
    (
        'abc.txt',
        '#t 1\ntxt1\ntxt11\ntxt111\n#t 2\n#t 3\ntxt3\ntxt33\n#t 4\n\n',
        '13\n#t 1\ntxt1\ntxt11\ntxt111\n#t 2\n#t 3\ntxt3\ntxt33\n#t 4\n\n\n1.....t 1\n5.....t 2\n6.....t 3\n9.....t 4'
    ),
    (
        'abc.txt',
        '',
        '3\n\n'
    )
]


@pytest.mark.parametrize('data', test_data)
def test_table_of_contents(data):
    # noinspection PyArgumentList
    try:
        with open(data[0], 'w') as file:
            file.write(data[1])
        table_of_contents.table_of_contents(data[0])
        with open(data[0], 'r') as file:
            assert file.read() == data[2]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0]):
            os.remove(data[0])
