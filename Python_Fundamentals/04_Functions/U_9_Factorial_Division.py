from math import factorial


def factorial_division(a, b):
    first_factorial = factorial(int(a))
    second_factorial = factorial(int(b))
    return first_factorial / second_factorial


x = input()
y = input()
print(f'{factorial_division(x, y):.2f}')
