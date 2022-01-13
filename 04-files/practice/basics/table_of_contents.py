def table_of_contents(filename):
    """Дописать оглавление и номер его начала в файл (см. _legend.md)"""
    lines, table, heads = [], [], []

    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        if line[0] == '#':
            heads.append(f'{lines.index(line)+1}.....{line[1:]}')

    for i in range(len(heads)):
        if i + 1 != len(heads):
            table.append(heads[i])
        else:
            table.append(heads[i][:-1])

    good = []
    for line in lines:
        if line != '\n':
            if '\n' not in line:
                line += '\n'
        else:
            good.append('\n')
        good.append(line)

    res = [str(len(good) + 2) + '\n'] + good + table

    with open(filename, 'w+', encoding='utf-8') as file:
        if good == []:
            file.writelines('3\n\n')
        else:
            file.writelines(res)
