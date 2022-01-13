import pytest
import os
import editor


test_data = [
    (
        """She sells seashells\nby the seashore""",
        """How can a clam cram in a clean cream can?\nShe sells seashells\nBy the seashore.""",
        [
            'append_line',
            'set_char 2 1 B',
            'set_text 3 How can a clam cram in a clean cream can?',
            'insert 2 16 .',
            'swap_lines 3 1',
            'swap_lines 3 2'
        ]
    ),
    (
        """""",
        """Hello\n\n\nworld""",
        [
            'append_lines 3',
            'set_text 1 Hello',
            'set_text 4 world'
        ]
    ),
    (
        """a\nb\nc\nd""",
        """any""",
        [
            'clear',
            'insert 1 1 y',
            'insert 1 1 n',
            'insert 1 1 a'
        ]
    ),
    (
        """a\nb\nc\nd""",
        """""",
        [
            'delete_line 1',
            'repeat 3'
        ]
    )
]


@pytest.mark.parametrize('data', test_data)
def test_edit(data):
    # noinspection PyArgumentList
    try:
        with open('file.txt', 'w') as file:
            file.write(data[0])
        editor.edit('file.txt', data[2])
        with open('file.txt', 'r') as file:
            assert data[1] == file.read()
    except Exception as e:
        pytest.fail(str(e))
    finally:
        if os.path.exists('file.txt'):
            os.remove('file.txt')
