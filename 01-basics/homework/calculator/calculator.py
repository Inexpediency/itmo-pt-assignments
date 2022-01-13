<<<<<<< HEAD
def find(arr, el):
    try:
        return arr.index(el)
    except ValueError:
        return -1


def apply_operation(op, left, right):
    if op == '+':
        return left + right
    if op == '-':
        return left - right
    if op == '*':
        return left * right
    if op == '/':
        return left / right


def calculate(expression):
    literals = list(expression.split())
    if len(literals) == 1:
        return float(expression)

    di = find(literals, '/')
    ui = find(literals, '*')
    pi = find(literals, '+')
    mi = find(literals, '-')

    if ui > di > 0:
        index = di
    elif di > ui > 0:
        index = ui
    elif di > 0:
        index = di
    elif ui > 0:
        index = ui
    else:
        index = max(di, ui, pi, mi)

    operation = literals[index]
    left = round(float(literals[index - 1]), 2)
    right = round(float(literals[index + 1]), 2)
    result = apply_operation(operation, left, right)

    literals.insert(index - 1, str(round(result, 2)))
    literals.pop(index)
    literals.pop(index)
    literals.pop(index)

    return calculate(' '.join(literals))
=======
def calculate(input_str):
    """Вычислить выражение, представленное в виде строки"""

    def math_action(a, b, symbol):

        if symbol == '*':
            return a * b
        elif symbol == '/':
            return a / b
        elif symbol == '+':
            return a + b
        else:
            return a - b

    def find_index(op1, op2, array):

        try:
            act1 = array.index(op1)
        except:
            act1 = 10e100

        try:
            act2 = array.index(op2)
        except:
            act2 = 10e100

        return min(act1, act2)

    def do_action(index, array):

        operation = array[index]

        a = float(array[index-1])
        b = float(array[index+1])
        elems = [a, b]

        computed = math_action([*elems], operation)
        array[index] = computed
        return array[:index-1] + [array[index]] + array[index+2:]

    parts = input_str.split()

    while ('*' in parts) or ('/' in parts):
        op_index = find_index('*', '/', parts)
        parts = do_action(op_index, parts)

    while ('+' in parts) or ('-' in parts):
        op_index = find_index('+', '-', parts)
        parts = do_action(op_index, parts)

    return round(float([*parts]), 2)
>>>>>>> origin/practice
