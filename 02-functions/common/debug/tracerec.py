from typing import Callable, List, Any, Optional


class __Counter:
    def __init__(self, base_indent: int):
        self.depth = 0
        self.space = '|' + ' ' * (base_indent - 1)

    def __enter__(self):
        self.depth += 1
        return self.depth

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.depth -= 1
        return self.depth

    def indent(self):
        return self.space * self.depth


def visualize(
        max_depth: Optional[int] = None,
        base_indent: int = 2,
        ignore_positional: Optional[List[int]] = None,
        ignore_named: Optional[List[str]] = None,
):
    if ignore_positional is None:
        ignore_positional = []
    if ignore_named is None:
        ignore_named = []
    ignore_positional = set(ignore_positional)
    ignore_named = set(ignore_named)

    def decorator(function: Callable[[Any], Any]):
        D = __Counter(base_indent)

        def __repr(name, args, kwargs_items):
            args = list(map(str, args))
            kwargs_items = list(map(lambda arg: f'{arg[0]}={arg[1]}', kwargs_items))
            return f'{name}({", ".join(args + kwargs_items)})'

        def __safe_print(*args, **kwargs):
            if max_depth is None or D.depth <= max_depth:
                print(*args, **kwargs)

        def __tracer(*args, **kwargs):
            nonlocal D
            data_args = [args[i] for i in range(len(args)) if i not in ignore_positional]
            data_kwargs = [arg for arg in kwargs.items() if arg[0] not in ignore_named]
            __safe_print(f'{D.indent()}{__repr(function.__name__, data_args, data_kwargs)}')
            with D:
                result = function(*args, **kwargs)
            __safe_print(f'{D.indent()}-> {result}')
            return result

        return __tracer

    return decorator
