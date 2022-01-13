import rprint
from pytest import mark
from common.test.run import CTEST, PTEST


# @formatter:off
@mark.parametrize(
    ['input_args', 'output'],
    [
        ([ [1, [], [2, [3, [4], 5]], [[[[6]]]]] ], list(range(1, 7))),
        ([ [] ], []),
        ([ [[[[]]]] ], []),
        ([ [1, [2, [3, [4, [5, [6], 7], 8], 9], 10], 11] ], list(range(1, 12))),
        ([ [1, 2, 3, 4, 5] ], list(range(1, 6))),
        ([ [[], [[]], [[[1]]], [[[[[[]]]]]]] ], [1]),
        ([ [1, [2, [[[3], [[]]]], 4], [[[5]]], [], 6] ], list(range(1, 7))),
    ]
)
# @formatter:on
def test_flatten(input_args, output):
    CTEST(rprint.flatten, input_args, output)


# @formatter:off
@mark.parametrize(
    ['input_args', 'output'],
    [
        ([ [1, [2, [3, 4], 5], [[[6, [7]]]]], 2 ], '[1, [2, [...], 5], [[...]]]'),
        ([ [], 10 ], '[]'),
        ([ [[[[]]]], 1 ], '[[...]]'),
        ([ [1, [2, [3, [4, [5, [6], 7], 8], 9], 10], 11], 3 ], '[1, [2, [3, [...], 9], 10], 11]'),
        ([ [1, 2, 3, 4, 5], 1 ], '[1, 2, 3, 4, 5]'),
        ([ [[], [[]], [[[1]]], [[[[[[]]]]]]], 0 ], '[...]'),
        ([ [1, [2, [[[3], [[]]]], 4], [[[5]]], [], 6], 2 ], '[1, [2, [...], 4], [[...]], [], 6]'),
    ]
)
# @formatter:on
def test_rprint(input_args, output):
    CTEST(rprint.rprint, input_args, output)


# @formatter:off
pretty_rprint_output = [
'''[
    [ 1 2 ]
    [ 3 ]
    [
        [ 4 ]
        5
        [
            6
            [ 7 ]
        ]
    ]
]''',
'''[
    [ ]
    10
]''',
'''[
    [
        [
            [ ]
        ]
    ]
]''',
'''[
    1
    [
        2
        [
            3
            [ 4 5 ]
            6
        ]
        7
    ]
    8
]''',
'''[ 1 2 3 4 5 ]''',
'''[
    [ ]
    [
        [ ]
    ]
    [
        [
            [ 1 ]
        ]
    ]
    [
        [
            2
            [ 3 4 ]
        ]
    ]
]''',
'''[
    1
    [
        2
        [
            [
                [ 3 ]
                [
                    [ ]
                ]
            ]
        ]
        4
    ]
    [
        [
            [ 5 ]
        ]
    ]
    [ ]
    6
]'''
]


@mark.parametrize(
    ['input_args', 'output'],
    [
        ([ [[1, 2], [3], [[4], 5, [6, [7]]]] ], pretty_rprint_output[0]),
        ([ [[], 10] ], pretty_rprint_output[1]),
        ([ [[[[]]]] ], pretty_rprint_output[2]),
        ([ [1, [2, [3, [4, 5], 6], 7], 8] ], pretty_rprint_output[3]),
        ([ [1, 2, 3, 4, 5] ], pretty_rprint_output[4]),
        ([ [[], [[]], [[[1]]], [[2, [3, 4]]]] ], pretty_rprint_output[5]),
        ([ [1, [2, [[[3], [[]]]], 4], [[[5]]], [], 6] ], pretty_rprint_output[6]),
    ]
)
# @formatter:on
def test_pretty_rprint(input_args, output):
    PTEST(rprint.pretty_rprint, input_args, output)
