def log_args(*args, mode, print=print):
    """Вывести все переданные аргументы в требуемом режиме"""
    if mode == 'args':
        print(' '.join(map(lambda x: str(x), args)))
    elif mode == 'list':
        print(list(args))
    elif mode == 'len':
        print(len(args))


def smart_filter(items, **kwargs):
    """Отфильтровать элементы, либо исключив лишние, либо оставив только нужные"""
    if ('include' not in kwargs.keys()) and ('exclude' not in kwargs.keys()):
        return None

    if 'include' in kwargs.keys():
        items = list(filter(lambda x: kwargs['include'](x), items))
    if 'exclude' in kwargs.keys():
        items = list(filter(lambda x: not kwargs['exclude'](x), items))

    return items


def smart_map(*args, **kwargs):
    """Заменить все строки в args, соответствующие ключам в kwargs, на их значения"""
    args = list(args)
    for i, arg in enumerate(args):
        if arg in kwargs.keys():
            args[i] = kwargs[arg]

    return args
