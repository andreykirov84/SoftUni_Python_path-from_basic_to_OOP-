def sum_numbers(a, b):
    return a + b


def subtract(c, d):
    return c - d


def add_and_subtract(a, b, c):
    x = sum_numbers(a, b)
    return subtract(x, c)


a = int(input())
b = int(input())
c = int(input())
print(add_and_subtract(a, b, c))

