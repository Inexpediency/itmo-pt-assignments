from abc import ABC, abstractmethod


class InvalidArguments(Exception):
    pass


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def add_args(self, args):
        pass

    @abstractmethod
    def add_kwargs(self, kwargs):
        pass

    @abstractmethod
    def get_name(self):
        pass


class CommandAdd(Command):
    _args = None

    def execute(self):
        return f'Added {len(self._args)} files'

    def add_args(self, args):
        self._validate_args(args)
        self._args = args

    def add_kwargs(self, kwargs):
        self._validate_kwargs(kwargs)

    def get_name(self):
        return 'add'

    @staticmethod
    def _validate_args(args):
        if not len(args):
            raise InvalidArguments

        for arg in args:
            if not isinstance(arg, str):
                raise InvalidArguments

    @staticmethod
    def _validate_kwargs(kwargs):
        if len(kwargs) != 0:
            raise InvalidArguments


class CommandCommit(Command):
    _args = None
    _kwargs = None

    def execute(self):
        self._validate_parameters()

        if len(self._args):
            return 'Commit successful'

        if '__amend' in self._kwargs:
            return 'Commit successful'

        if 'message' in self._kwargs:
            return 'Commit successful'

        raise InvalidArguments

    def add_args(self, args):
        self._validate_args(args)
        self._args = args

    def add_kwargs(self, kwargs):
        self._validate_kwargs(kwargs)
        self._kwargs = kwargs

    def get_name(self):
        return 'commit'

    def _validate_parameters(self):
        arguments_count = len(self._args) + len(self._kwargs)
        if arguments_count == 0 or arguments_count > 1:
            raise InvalidArguments

    @staticmethod
    def _validate_args(args):
        if len(args) > 1:
            raise InvalidArguments

        if len(args) and not isinstance(args[0], str):
            raise InvalidArguments

    @staticmethod
    def _validate_kwargs(kwargs):
        if len(kwargs) > 1:
            raise InvalidArguments

        validation_rules = {
            '__amend': (bool, True),
            'message': (str, None),
        }

        validate_flags(validation_rules, kwargs)


class CommandPush(Command):
    _default_branch = 'main'

    _args = None
    _kwargs = None

    def execute(self):
        self._validate_destination()

        response = []
        if '__force' in self._kwargs.keys():
            response.extend(['Force', 'push'])
        else:
            response.append('Push')

        remote, branch = self._get_destination()
        response.extend(['to', f'{remote}/{branch}'])
        response.append('successful')

        return ' '.join(response)

    def add_args(self, args):
        self._validate_args(args)
        self._args = args

    def add_kwargs(self, kwargs):
        self._validate_kwargs(kwargs)
        self._kwargs = kwargs

    def get_name(self):
        return 'push'

    def _get_destination(self):
        if len(self._args):
            if len(self._args) == 1:
                remote, branch = self._args[0], self._default_branch
            else:
                remote, branch = self._args
        else:
            if 'remote' in self._kwargs.keys():
                remote = self._kwargs['remote']
            else:
                raise InvalidArguments

            if 'branch' in self._kwargs.keys():
                branch = self._kwargs['branch']
            else:
                branch = self._default_branch

        return remote, branch

    def _validate_destination(self):
        destination_length_in_kwargs = 0
        for k, _ in self._kwargs.items():
            if k in ['remote', 'branch']:
                destination_length_in_kwargs += 1

        if len(self._args) and destination_length_in_kwargs:
            raise InvalidArguments

    @staticmethod
    def _validate_args(args):
        if not (0 <= len(args) <= 2):
            raise InvalidArguments

        for arg in args:
            if not isinstance(arg, str):
                raise InvalidArguments

    @staticmethod
    def _validate_kwargs(kwargs):
        validation_rules = {
            'remote': (str, None),
            'branch': (str, None),
            '__force': (bool, True),
            '__set_upstream': (bool, True)
        }

        validate_flags(validation_rules, kwargs)


def validate_flags(flags, rules):
    for k, v in flags.items():
        if k not in rules.keys():
            raise InvalidArguments
        if not isinstance(v, rules[k][0]):
            raise InvalidArguments
        if rules[k][1] is not None and v != rules[k][1]:
            raise InvalidArguments


def get_commands():
    return [CommandAdd(), CommandCommit(), CommandPush()]


def git(command_name: str, *args, **kwargs):
    for c in get_commands():
        if c.get_name() == command_name:
            try:
                c.add_args(args)
                c.add_kwargs(kwargs)

                return c.execute()
            except InvalidArguments:
                return None

    return 'Unknown command'
