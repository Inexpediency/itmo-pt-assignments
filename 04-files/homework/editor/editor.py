from typing import List


class Editor:
    _filename: str = None
    _data: List[str] = None

    def load(self, filename):
        with open(filename, 'r') as f:
            self._data = f.read().split('\n')
            if not len(self._data):
                self._data = ['']

    def dump(self, filename):
        with open(filename, 'w') as f:
            f.write('\n'.join(self._data))

    def set_text(self, line_number, text):
        self._data[line_number] = text

    def set_char(self, line_number, char_position, char):
        line = list(self._data[line_number])
        line[char_position] = char
        self._data[line_number] = ''.join(line)

    def insert(self, line_number, char_position, char):
        self._data[line_number] = self._data[line_number][:char_position] + \
                                  char + self._data[line_number][char_position:]

    def insert_line(self, line_number):
        self._data.insert(line_number, '')

    def append(self, line_number, char):
        self._data[line_number].append(char)

    def append_line(self):
        self._data.append('')

    def append_lines(self, lines_count):
        self._data.extend([''] * lines_count)

    def delete_line(self, line_number):
        self._data = self._data[:line_number] + self._data[line_number + 1:]

    def delete_lines(self, from_line, to_line):
        self._data = self._data[:from_line] + self._data[to_line + 1:]

    def delete_char(self, line_number, char_position):
        self._data[line_number] = \
            self._data[line_number][:char_position] + self._data[line_number][char_position + 1:]

    def find_and_remove(self, text):
        self._data = [line.replace(text, '') for line in self._data]

    def delete_lines_having_text(self, text):
        self._data = list(filter(lambda line: text not in line, self._data))

    def duplicate_line(self, line_number):
        self._data.insert(line_number + 1, self._data[line_number])

    def clear(self):
        self._data = ['']

    def swap_lines(self, first_line, second_line):
        self._data[first_line], self._data[second_line] = self._data[second_line], self._data[first_line]


def execute_command(editor, command, args):
    if command == 'set_text':
        editor.set_text(int(args[0]) - 1, ' '.join(args[1:]))
    elif command == 'set_char':
        editor.set_char(int(args[0]) - 1, int(args[1]) - 1, args[2])
    elif command == 'insert':
        editor.insert(int(args[0]) - 1, int(args[1]) - 1, ' '.join(args[2:]))
    elif command == 'insert_line':
        editor.insert_line(int(args[0]) - 1)
    elif command == 'append':
        editor.append(int(args[0]), ' '.join(args[1:]))
    elif command == 'append_line':
        editor.append_line()
    elif command == 'append_lines':
        editor.append_lines(int(args[0]))
    elif command == 'delete_line':
        editor.delete_line(int(args[0]) - 1)
    elif command == 'delete_lines':
        editor.delete_lines(int(args[0]), int(args[1]) - 1)
    elif command == 'delete_char':
        editor.delete_char(int(args[0]) - 1, int(args[1]) - 1)
    elif command == 'find_and_remove':
        editor.find_and_remove(*args)
    elif command == 'delete_lines_having_text':
        editor.delete_lines_having_text(*args)
    elif command == 'duplicate_line':
        editor.duplicate_line(int(args[0]) - 1)
    elif command == 'clear':
        editor.clear()
    elif command == 'swap_lines':
        editor.swap_lines(int(args[0]) - 1, int(args[1]) - 1)
    else:
        raise Exception('invalid command')


def get_command_and_args(row_command):
    split_command = row_command.split()

    return split_command[0], split_command[1:]


def edit(filename, commands: List[str]):
    editor = Editor()
    editor.load(filename)

    commands = [get_command_and_args(row_command) for row_command in commands]

    for command_index, command in enumerate(commands):
        command_name, command_args = command
        if command_name == 'repeat':
            for i in range(int(command_args[0])):
                execute_command(editor, *commands[command_index - 1])
        else:
            execute_command(editor, command_name, command_args)

    editor.dump(filename)
