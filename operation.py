from math import sin, cos, tan

def simple_operations():
    try:
        first_num = float(input('Type 1st number:').strip())
        second_num = float(input('Type 2nd number:').strip())
        operation = input('''Choose operation:
        Available options:
                        '+'    '-'    '*'    '/' ''').strip()
        if operation == '+':
            result = first_num + second_num
        elif operation == '-':
            result = first_num - second_num
        elif operation == '*':
            result = first_num * second_num
        elif operation == '/':
            try:
                result = first_num / second_num
            except ZeroDivisionError:
                result = 'Error!'
                print('Division by zero!')
        return '{} {} {} = {}'.format(first_num, operation, second_num, result)
    except Exception:
        print('Unexpected Error')


def trigonometric():
    num = float(input('Type number:').strip())
    operation = input('''Choose operation:
        Available options:
                            'sin'    'cos'    'tan' ''').lower().strip()
    if operation == 'sin':
        result = sin(num)
    elif operation == 'cos':
        result = cos(num)
    elif operation == 'tan':
        result = tan(num)
    return '{} ({}) = {}'.format(operation, num, result)


# simple_oper_result = simple_operations()
# print(simple_oper_result)
#
# trigomometric_result = trigonometric()
# print(trigomometric_result)

