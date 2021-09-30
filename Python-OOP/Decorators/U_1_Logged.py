def logged(function):
    def wrapper(*args):
        result = function(*args)
        result_string = f'it returned {result}'
        name = f'you called {function.__name__}'
        return f'{name}{args}\n{result_string}'
    return wrapper


# @logged
# def func(*args):
#     return 3 + len(args)
#
#
# print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))


# print(func.__name__)
# print()
# you called func(4, 4, 4)
# it returned 6
