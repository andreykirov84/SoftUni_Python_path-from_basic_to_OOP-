def data_type(input_type, input_value):
    result = None
    if input_type == 'int':
        result = 2 * int(input_value)
    elif input_type == 'real':
        result = f'{1.5 * float(input_value):.2f}'
    elif input_type == 'string':
        result = '$' + input_value + '$'

    return result


print(data_type(input(), input()))
