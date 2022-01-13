from typing import Callable, Optional, List, Any, Dict
from pytest import fail
from copy import deepcopy

from .redirect import Input, Print


def CTEST(
        function: Callable,
        input_args: List[Any], output: Any,
        input_kwargs: Optional[Dict[str, Any]] = None,
):
    if input_kwargs is None:
        input_kwargs = dict()
    input_copy = deepcopy(input_args)
    assert function(*input_args, **input_kwargs) == output
    assert input_args == input_copy


def PTEST(
        function: Callable,
        input_args: List[Any], output: str,
        input_kwargs: Optional[Dict[str, Any]] = None,
        call_limit: Optional[int] = None, redirect_input: bool = False,
):
    if input_kwargs is None:
        input_kwargs = dict()
    args, kwargs = input_args, input_kwargs
    if redirect_input:
        assert all(map(lambda item: type(item) is str, input_args))
        args, kwargs = [], {'input': Input(input_args)}
    printer = Print(call_limit)
    kwargs['print'] = printer
    function(*args, **kwargs)
    assert printer.get() == output
