import recurrent
from pytest import mark
from common.test.run import CTEST


# @formatter:off
@mark.parametrize(
    ['input_args', 'output'],
    [
        ([ 0 ], 0),
        ([ 1 ], 1),
        ([ 2 ], 2),
        ([ 3 ], 3),
        ([ 4 ], 4),
        ([ 100 ], 100),
        ([ 137 ], 137),
        ([ 211 ], 211)
    ]
)
# @formatter:on
def test_identity(input_args, output):
    CTEST(recurrent.identity, input_args, output)


# @formatter:off
@mark.parametrize(
    ['input_args', 'output'],
    [
        ([ 1 ], 0),
        ([ 2 ], 1),
        ([ 3 ], 1),
        ([ 4 ], 2),
        ([ 100 ], 6),
        ([ 127 ], 6),
        ([ 128 ], 7),
        ([ 256 ], 8)
    ]
)
# @formatter:on
def test_log2(input_args, output):
    CTEST(recurrent.log2, input_args, output)


# @formatter:off
@mark.parametrize(
    ['input_args', 'output'],
    [
        ([ 0 ], 0),
        ([ 1 ], [0]),
        ([ 2 ], [[0]]),
        ([ 3 ], [[[0]]]),
        ([ 4 ], [[[[0]]]]),
        ([ 10 ], [[[[[[[[[[0]]]]]]]]]]),
        ([ 11 ], [[[[[[[[[[[0]]]]]]]]]]]),
        ([ 12 ], [[[[[[[[[[[[0]]]]]]]]]]]])
    ]
)
# @formatter:on
def test_push(input_args, output):
    CTEST(recurrent.push, input_args, output)
