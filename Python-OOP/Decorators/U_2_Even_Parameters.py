def even_parameters(function):
    def wrapper(*args):
        is_even = True
        for i in args:
            if isinstance(i, float) or isinstance(i, int):
                if i % 2 != 0:
                    is_even = False
                    break
            else:
                is_even = False
                break
        if is_even:
            return function(*args)
        else:
            return 'Please use only even numbers!'
    return wrapper


# @even_parameters
# def add(a, b):
#     return a + b
#
#
# print(add(2, 4))
# print(add("Peter", 1))

@even_parameters
def func(*args):
    return sum(args)


print(func(4, "4", 4))

# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
#
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))


