import pytest
import os
import config


repeat_data = [
    (
        'test.ini',
        '[DEFAULT]\nstr = hello world\ncount = 3\n',
        'hello worldhello worldhello world'
    ),
    (
        'test.ini',
        '[DEFAULT]\nstr: nana\ncount: 2\n',
        'nananana'
    )
]


@pytest.mark.parametrize('data', repeat_data)
def test_repeat(data):
    # noinspection PyArgumentList
    try:
        with open(data[0], 'w') as file:
            file.write(data[1])
        assert config.repeat(data[0]) == data[2]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(data[0]):
            os.remove(data[0])


connection_config_file = 'connections.ini'
connection_config_content = """[DEFAULT]
ip = 127.0.0.1
port = 8888

[John]
ip = 1.1.1.1
port = 7963

[Jerry]
ip = 37.182.55.11
port = 21001

[Tommy]
ip = 37.182.55.11
port = 21002

[Anna]
ip = 127.0.0.1
port = 7878

[Maria]
ip: 39.111.44.121
port: 1111
"""

connection_test_data = [
    ('John', ('1.1.1.1', '7963')),
    ('Pete', ('127.0.0.1', '8888')),
    ('Anna', ('127.0.0.1', '7878')),
    ('Jerry', ('37.182.55.11', '21001')),
    ('Tommy', ('37.182.55.11', '21002')),
    ('Arbababa', ('127.0.0.1', '8888'))
]


@pytest.mark.parametrize('data', connection_test_data)
def test_get_connection_info(data):
    # noinspection PyArgumentList
    try:
        with open(connection_config_file, 'w') as file:
            file.write(connection_config_content)
        assert config.get_connection_info(connection_config_file, data[0]) == data[1]
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists(connection_config_file):
            os.remove(connection_config_file)
