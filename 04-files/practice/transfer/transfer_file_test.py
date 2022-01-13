import os
import pathlib
import multiprocessing
import random
import shutil
import time
from pytest import mark

from transfer_file import run_receiver, run_sender


def join_and_terminate(thread: multiprocessing.Process):
    thread.join(20.0)
    if thread.is_alive():
        thread.terminate()
        raise TimeoutError(f'thread {thread} timed out')


def gen_random(size):
    a = [random.randint(0, 255) for _ in range(size)]
    return bytes(a)


@mark.parametrize('source_path, target_path, data_gen', [
    ('practice/transfer/transfer_file.py', 'tmpdest', None),
    ('practice/transfer/transfer_file_test.py', 'tmpdest', None),
    ('practice/_legend.md', '', None),
    ('sandbox/data.txt', 'tmp1/tmp2/data', lambda: gen_random(0)),
    ('sandbox/data.txt', 'tmp1/tmp2/data', lambda: gen_random(1)),
    ('sandbox/data.txt', 'tmp1/tmp2/data', lambda: gen_random(256)),
    ('sandbox/dir1/dir2/temp/file-русские-буквы.unknown', 'tmpdest/a/b/c/d/e/f', lambda: gen_random(2 ** 10)),
    ('sandbox/dir1/dir2/temp/file-babc6dfec6b8.unknown', 'tmpdest/a/b/c/d/e/f', lambda: gen_random(2 ** 17 + 1)),
])
def test_transfer_file(source_path: str, target_path: str, data_gen):
    loc = pathlib.Path('.').absolute()
    while not loc.name.startswith('assignment-04-files'):
        os.chdir('..')
        loc = loc.parent

    source = pathlib.Path(source_path).absolute()
    tmpdir = pathlib.Path('tmpdir').absolute()
    to_remove = [tmpdir]
    target = tmpdir / target_path
    os.makedirs(target, exist_ok=True)
    if data_gen is not None:
        data = data_gen()
        source_loc = source
        while not source_loc.parent.exists():
            source_loc = source_loc.parent
        to_remove.append(source_loc)
        os.makedirs(source.parent, exist_ok=True)
        with open(str(source), 'wb') as f:
            f.write(data)
    else:
        with open(str(source), 'rb') as f:
            data = f.read()

    rec = multiprocessing.Process(target=run_receiver, args=(f'tmpdir/{target_path}',))
    snd = multiprocessing.Process(target=run_sender, args=(source_path,))
    rec.start()
    time.sleep(1)
    snd.start()
    join_and_terminate(snd)
    join_and_terminate(rec)

    target_file = target / source.name
    if not target_file.exists() or not target_file.is_file():
        new_data = None
    else:
        with open(str(target_file), 'rb') as f:
            new_data = f.read()

    for loc in to_remove:
        if loc.is_file():
            os.remove(loc)
        else:
            shutil.rmtree(loc)

    assert data == new_data
