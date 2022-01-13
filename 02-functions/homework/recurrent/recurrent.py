from typing import Callable, Any


def __recurrent(
        n: Any,
        stop_condition: Callable[[Any], bool],
        transform: Callable[[Any], Any],
        value: Callable[[Any], Any]
) -> Any:
    """Это вспомогательная функция, не надо ее менять"""
    if stop_condition(n):
        return n
    return __recurrent(transform(n), stop_condition, transform, value) + value(n)


def identity(n):
    """Вернуть число n, используя __recurrent"""
    return __recurrent(
        n,
        stop_condition=lambda x: x == 0,
        transform=lambda x: x - 1,
        value=lambda x: 1
    )


def log2(n):
    """Вернуть округленный вниз двоичный логарифм n, используя __recurrent"""
    return __recurrent(
        n,
        lambda x: x < 1,
        lambda x: x // 2,
        lambda x: 1 if x > 1 else 0
    )


def push(n):
    """Вернуть массив, в котором единственное число 0 лежит на глубине n"""

    depth = lambda L: isinstance(L, list) and max(map(depth, L)) + 1

    return __recurrent(
        n,
        lambda x: depth(x) == n,
        lambda x: [x] if isinstance(x, list) else [0],
        lambda x: []
    )
