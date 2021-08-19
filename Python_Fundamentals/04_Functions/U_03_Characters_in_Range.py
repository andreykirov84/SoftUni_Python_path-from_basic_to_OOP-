def ascii_char_range(a, b):
    number_one = ord(a)
    number_two = ord(b)
    result = chr(number_one + 1)
    separator = ' '
    for i in range(number_one + 2, number_two):
        result += separator + chr(i)
    return result


a = input()
b = input()
print(ascii_char_range(a, b))
