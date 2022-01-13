import args
from pytest import mark
from common.test.run import CTEST, PTEST


# @formatter:off
@mark.parametrize(
    ['input_args', 'input_kwargs', 'output'],
    [
        ([ 0, 1, 2 ], { 'mode': 'args' }, '0 1 2'),
        ([ 0, 1, 2 ], { 'mode': 'list' }, '[0, 1, 2]'),
        ([ 0, 1, 2 ], { 'mode': 'len' }, '3'),
        ([ ], { 'mode': 'args' }, ''),
        ([ ], { 'mode': 'list' }, '[]'),
        ([ ], { 'mode': 'len' }, '0'),
        ([ -1 ], { 'mode': 'args' }, '-1'),
        ([ -1 ], { 'mode': 'list' }, '[-1]'),
        ([ -1 ], { 'mode': 'len' }, '1'),
    ]
)
# @formatter:on
def test_log_args(input_args, input_kwargs, output):
    PTEST(args.log_args, input_args, output, input_kwargs=input_kwargs)


# @formatter:off
@mark.parametrize(
    ['input_args', 'input_kwargs', 'output'],
    [
        ([ [1, 2, 3, 4] ], { 'include': lambda x: x % 2 == 0 }, [2, 4]),
        ([ [1, 2, 3, 4] ], { 'exclude': lambda x: x % 2 == 0 }, [1, 3]),
        ([ [1, 2, 3, 4] ], {}, None),
        ([ [1, 2, 3, 4] ], { 'inexclude': lambda x: x }, None),
        ([ [5, 4, 3, 2, 1] ], { 'include': lambda x: x % 3 != 0, 'exclude': lambda x: x % 2 == 0 }, [5, 1]),
        ([ [1, 2, 3, 4] ], { 'exclude': lambda x: False, 'include': lambda x: True }, [1, 2, 3, 4]),
        ([ [] ], { 'exclude': lambda x: False, 'include': lambda x: True }, []),
        ([ [1, 2, 3, 4] ], { 'exclude': lambda x: True, 'include': lambda x: False }, []),
        ([ [1, 2, 2, 1] ], { 'exclude': lambda x: False, 'include': lambda x: x % 2 == 0 }, [2, 2]),
    ]
)
# @formatter:on
def test_smart_filter(input_args, input_kwargs, output):
    CTEST(args.smart_filter, input_args, output, input_kwargs=input_kwargs)


# @formatter:off
@mark.parametrize(
    ['input_args', 'input_kwargs', 'output'],
    [
        ([ 'a', 'b', 'c', 'd' ], { }, ['a', 'b', 'c', 'd']),
        ([ 'a', 'b', 'c', 'd' ], { 'c': 1 }, ['a', 'b', 1, 'd']),
        ([ 'd', 'b', 'c', 'd' ], { 'd': 'a' }, ['a', 'b', 'c', 'a']),
        ([ 'c', 'b', 'b', 'c' ], { 'c': 'b', 'b': 'c' }, ['b', 'c', 'c', 'b']),
        ([ 'a', 'b', 'c', 'd' ], { 'z': 'd' }, ['a', 'b', 'c', 'd']),
        ([ 'a', 'b', 'c', 'd' ], { 'z': 'd', 'd': 'z' }, ['a', 'b', 'c', 'z']),
        ([ 'a', 'b', 'c', 'd' ], { 'a': 'z', 'b': 'z', 'c': 'z', 'd': 'z', 'z': 0 }, ['z', 'z', 'z', 'z']),
        ([ 'a', 'b', 'c', 'd' ], { 'a': '@', '@': '@@', '@@': 'a' }, ['@', 'b', 'c', 'd']),
        ([ 'a' ], { 'a': '@', 'b': 'a' }, ['@']),
        ([ ], { 'a': '@', 'b': 'a' }, []),
    ]
)
# @formatter:on
def test_smart_map(input_args, input_kwargs, output):
    CTEST(args.smart_map, input_args, output, input_kwargs=input_kwargs)
