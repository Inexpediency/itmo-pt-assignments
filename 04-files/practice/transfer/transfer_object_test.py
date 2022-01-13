import copy
import os
import pathlib
import multiprocessing
import random
import shutil
import time
from pytest import mark

from transfer_object import run_receiver, run_sender


def join_and_terminate(thread: multiprocessing.Process):
    thread.join(20.0)
    if thread.is_alive():
        thread.terminate()
        raise TimeoutError(f'thread {thread} timed out')


def randword(size):
    return ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(size)])


def gen_random(size):
    a = {}
    if size == 0:
        return a
    for i in range(size):
        if random.randint(0, 1) == 0:
            a[randword(size)] = [gen_random(random.randint(0, size - 1))
                                 for _ in range(random.randint(0, int(size ** 0.5 + 1)))]
        else:
            a[randword(size)] = gen_random(random.randint(0, size - 1))
    return a


def receive(target):
    target['result'] = run_receiver()


@mark.parametrize('obj', [
    1,
    -2e100,
    {'x': 'y', 'z': 2},
    'x + y + z = t',
    [1, 2, 'aa', {'x': 'y'}, [[[]]], [[{}, {'a': 'b'}]]],
    gen_random(3),
    gen_random(10),
    gen_random(7),
])
def test_transfer_object(obj):
    data = copy.deepcopy(obj)
    manager = multiprocessing.Manager()
    res = manager.dict()
    rec = multiprocessing.Process(target=receive, args=(res,))
    snd = multiprocessing.Process(target=run_sender, args=(obj,))
    rec.start()
    time.sleep(1)
    snd.start()
    join_and_terminate(snd)
    join_and_terminate(rec)
    assert data == res['result']
