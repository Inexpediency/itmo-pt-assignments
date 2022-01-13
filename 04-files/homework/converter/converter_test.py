import pytest
import os
import json
import converter

fdtxt = [
    """If a <FF0000>dog</> chews shoes, <99FFA1>whose shoes</> does he choose?""",
    """Why <AABBCC>not</>?\n<FFFFFF>THAT's</> why!""",
    """No formatting""",
    """a <lt> 5 <lt> 8""",
    """Multiline\ntext\n<111122> with </>formatting""",
    """""",
]

fdjson = [
    """
    {
      "spans": [
        { "text": "If a " },
        {
          "text": "dog",
          "color": "#FF0000"
        },
        { "text": " chews shoes, " },
        {
          "text": "whose shoes",
          "color": "#99FFA1"
        },
        { "text": " does he choose?" }
      ]
    }
    """,
    """
    {
        "spans": [
            { "text": "Why " },
            {
                "text": "not",
                "color": "#AABBCC"
            },
            { "text": "?\\n" },
            {
                "text": "THAT's",
                "color": "#FFFFFF"
            },
            { "text": " why!" }
        ]
    }
    """,
    """
    {
        "spans": [
            { "text": "No formatting" }
        ]
    }
    """,
    """
    {
        "spans": [
            { "text": "a < 5 < 8" }
        ]
    }
    """,
    """
    {
        "spans": [
            { "text": "Multiline\\ntext\\n" },
            {
                "text": " with ",
                "color": "#111122"
            },
            { "text": "formatting" }
        ]
    }
    """,
    """
    {
        "spans": [
            { "text": "" }
        ]
    }
    """
]

fdbin = [
    ("If a dog chews shoes, whose shoes does he choose?", [
        (5, 7, 'FF0000'),
        (22, 32, '99FFA1'),
    ]),
    ("Why not?\nTHAT's why!", [
        (4, 6, 'AABBCC'),
        (9, 14, 'FFFFFF'),
    ]),
    ("No formatting", []),
    ("a < 5 < 8", []),
    ("Multiline\ntext\n with formatting", [
        (15, 20, '111122'),
    ]),
    ("", [])
]


test_data = list(zip(fdtxt, fdjson, fdbin))


def make_text(filename, data):
    with open(filename, 'w') as file:
        file.write(data)


def make_bin(filename, data):
    with open(filename, 'wb') as file:
        txt_bytes = data[0].encode('utf-8')
        file.write(len(txt_bytes).to_bytes(4, byteorder='big', signed=True))
        file.write(txt_bytes)
        file.write(len(data[1]).to_bytes(4, byteorder='big', signed=True))
        for span in data[1]:
            file.write(span[0].to_bytes(4, byteorder='big', signed=True))
            file.write(span[1].to_bytes(4, byteorder='big', signed=True))
            file.write(span[2].encode('ascii'))


def file_count():
    return sum([len(files) for r, d, files in os.walk(".")])


def cleanup(filenames):
    for fname in filenames:
        if os.path.exists(fname):
            os.remove(fname)


def compare_txt(filename1, filename2):
    with open(filename1, 'r') as file:
        s1 = file.read()
    with open(filename2, 'r') as file:
        s2 = file.read()
    return s1 == s2


def compare_json(filename1, filename2):
    with open(filename1, 'r') as file:
        s1 = json.loads(file.read())
    with open(filename2, 'r') as file:
        s2 = json.loads(file.read())
    return s1 == s2


def compare_bin(filename1, filename2):
    with open(filename1, 'rb') as file:
        data1 = file.read()
    with open(filename2, 'rb') as file:
        data2 = file.read()
    return data1 == data2


def compare_files(filename1, filename2):
    if filename1.endswith('.fdtxt'):
        return compare_txt(filename1, filename2)
    elif filename1.endswith('.fdjson'):
        return compare_json(filename1, filename2)
    else:
        return compare_bin(filename1, filename2)


@pytest.mark.parametrize('data', test_data)
def test_convert(data):
    fc1 = file_count()
    try:
        make_text('in.fdtxt', data[0])
        make_text('in.fdjson', data[1])
        make_bin('in.fdbin', data[2])

        for in_format in ['fdtxt', 'fdjson', 'fdbin']:
            for out_format in ['fdtxt', 'fdjson', 'fdbin']:
                converter.convert('in.' + in_format, 'out.' + out_format)
                assert compare_files('in.' + out_format, 'out.' + out_format)
    except Exception as e:
        pytest.fail(str(e))
    finally:
        cleanup([
            'in.fdtxt',
            'in.fdjson',
            'in.fdbin',
            'out.fdtxt',
            'out.fdjson',
            'out.fdbin'
        ])
    fc2 = file_count()
    assert fc1 == fc2
