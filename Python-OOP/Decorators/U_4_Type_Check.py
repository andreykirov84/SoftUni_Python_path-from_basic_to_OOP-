def type_check(fn_type):
    def decorator(func):
        def wrapped(*args):
            correct_type = True
            for i in args:
                if not isinstance(i, fn_type):
                    correct_type = False
                    break
            if correct_type:
                return func(*args)
            else:
                return "Bad Type"
        return wrapped
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
# 4
# Bad Type

