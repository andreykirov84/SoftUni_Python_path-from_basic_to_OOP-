number_one = int(input())
number_two = int(input())
operator = input()
result = 0
type = None


def is_even(number):
    type = 'odd'
    if number % 2 == 0:
        type = 'even'
    return type


if operator == '+':
    result = number_one + number_two
    type = is_even(result)
    print(f'{number_one} {operator} {number_two} = {result} - {type}')

elif operator == '-':
    result = number_one - number_two
    type = is_even(result)
    print(f'{number_one} {operator} {number_two} = {result} - {type}')

elif operator == '*':
    result = number_one * number_two
    type = is_even(result)
    print(f'{number_one} {operator} {number_two} = {result} - {type}')

elif operator == '/':
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one / number_two
        print(f"{number_one} / {number_two} = {result:.2f}")

elif operator == '%':
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one % number_two
        print(f"{number_one} % {number_two} = {result}")
