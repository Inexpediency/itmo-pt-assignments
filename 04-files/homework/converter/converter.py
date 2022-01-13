import json


HEX_COLOR_LENGTH = 8


def is_hex(line):
    alphabet = 'ABCDEF0123456789<>'

    for char in line:
        if char not in alphabet:
            return False

    return len(line) == HEX_COLOR_LENGTH


def read_fdtxt(file, input_data=''):
    if not input_data:
        input_data = ''.join(file.readlines())
    input_data = input_data.replace('<lt>', '<').split('</>')

    data = []
    for x in input_data:
        text, colored, color = '', '', ''
        for i in range(len(x)):
            if x[i] == '<' and is_hex(x[i:i + HEX_COLOR_LENGTH]):
                color = x[i:i + HEX_COLOR_LENGTH]
                text, colored = x.split(color)

        if color:
            data.extend([text, color, colored, '</>'])
        else:
            data.append(x)

    return data


def read_fdjson(file):
    input_data = ''.join(file.readlines())
    spans = json.loads(input_data, strict=False)["spans"]
    result = []
    for span in spans:
        text = span["text"].replace('<lt>', '<')
        if "color" not in span.keys():
            result.append(text)
        else:
            result.append('<' + span["color"][1:] + '>')
            result.append(text)
            result.append('</>')
    return result


def read_fdbin(file):
    data = []
    n_bytes = int.from_bytes(file.read(4), 'big', signed=True)
    text = file.read(n_bytes).decode('utf-8').replace('<lt>', '<')
    colored_count = int.from_bytes(file.read(4), 'big', signed=True)

    for _ in range(colored_count):
        from_index = int.from_bytes(file.read(4), 'big', signed=True)
        to_index = int.from_bytes(file.read(4), 'big', signed=True)
        color = '<' + file.read(6).decode('ascii') + '>'
        span = text[from_index:to_index + 1]
        data.append([color, span])

    for x in data:
        color, span = x
        text = text.replace(span, color + span + '</>')

    return read_fdtxt(file, text)


def create_fdtxt(input_data):
    result = []

    for part in input_data:
        if not is_hex(part) and part != '</>':
            result.append(part.replace('<', '<lt>'))
        else:
            result.append(part)

    return ''.join(result)


def create_fdjson(input_data):
    result = {"spans": []}

    input_data = [x for x in input_data if x != '</>']
    if not is_hex(input_data[0]):
        result["spans"].append({"text": input_data[0]})

    for i in range(1, len(input_data)):
        if is_hex(input_data[i - 1]):
            result["spans"].append({"text": input_data[i], "color": f'#{input_data[i - 1][1:-1]}'})
        elif not is_hex(input_data[i]):
            result["spans"].append({"text": input_data[i]})

    return json.dumps(result, indent=4)


def create_fdbin(input_data):
    colored_count = input_data.count('</>')
    input_data = [x for x in input_data if x != '</>']
    text = ''.join([x for x in input_data if not is_hex(x)])
    text_length_in_bytes = len(text).to_bytes(4, 'big', signed=True)
    text = text.encode('utf-8')
    data = []
    for _ in range(colored_count):
        for i in range(1, len(input_data)):
            if is_hex(input_data[i - 1]):
                color = input_data[i - 1][1:-1].encode('ascii')
                input_data.remove(input_data[i - 1])

                from_index = len(''.join(input_data[:i - 1]))
                to_index = len(''.join(input_data[i - 1]))

                data.append(from_index.to_bytes(4, 'big', signed=True))
                data.append((from_index + to_index - 1).to_bytes(4, 'big', signed=True))
                data.append(color)

                break

    colored_count = colored_count.to_bytes(4, 'big', signed=True)

    return text_length_in_bytes, text, colored_count, *data


def convert(input_file_path, output_file_path):
    data = []

    input_extension = input_file_path.split('.')[-1]
    output_extension = output_file_path.split('.')[-1]

    if input_extension == 'fdtxt':
        with open(input_file_path, 'r+') as inp:
            data = read_fdtxt(inp)
    elif input_extension == 'fdjson':
        with open(input_file_path, 'r+') as inp:
            data = read_fdjson(inp)
    elif input_extension == 'fdbin':
        with open(input_file_path, 'rb+') as inp:
            data = read_fdbin(inp)
    if output_extension == 'fdtxt':
        with open(output_file_path, 'w+') as out:
            out.write(create_fdtxt(data))
    elif output_extension == 'fdjson':
        with open(output_file_path, 'w+') as out:
            out.write(create_fdjson(data))
    elif output_extension == 'fdbin':
        with open(output_file_path, 'wb+') as out:
            for x in create_fdbin(data):
                out.write(x)

>> >> >> > origin / homework
