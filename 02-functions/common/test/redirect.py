from typing import Callable, Optional, List
from io import StringIO


class Input:
    def __init__(self, data: List[str], expect_prompt: Optional[str] = None):
        self.data: List[str] = []
        self.expect_prompt: Optional[int] = None
        self.calls = 0
        self.setup(data, expect_prompt)

    def setup(self, data: List[str], expect_prompt: Optional[str]):
        self.calls = 0
        self.data = data
        self.expect_prompt = expect_prompt

    def __call__(self, *args, **kwargs):
        if self.expect_prompt is None:
            assert len(args) + len(kwargs) == 0
            return

        assert len(args) + len(kwargs) == 1
        if len(args) > 0:
            assert args[0] == self.expect_prompt
        else:
            assert kwargs.keys()[0] == 'prompt'
            assert kwargs['prompt'] == self.expect_prompt

        assert self.calls < len(self.data)
        self.calls += 1
        return self.data[self.calls - 1]


class Print:
    def __init__(self, call_limit: Optional[int] = None):
        self.call_limit: Optional[int] = None
        self.stream: Optional[StringIO] = None
        self.calls = 0
        self.setup(call_limit)

    def setup(self, call_limit: Optional[int]):
        self.call_limit = call_limit
        self.stream = StringIO()
        self.calls = 0

    def __call__(self, *args, **kwargs):
        assert 'file' not in kwargs.keys()
        kwargs['file'] = self.stream
        self.calls += 1
        if self.call_limit is not None:
            assert self.calls <= self.call_limit
        print(*args, **kwargs)

    def get(self):
        return self.stream.getvalue().rstrip()
