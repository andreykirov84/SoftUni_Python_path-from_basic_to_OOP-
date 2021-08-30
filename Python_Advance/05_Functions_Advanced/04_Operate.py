def operate(x, res_func=0, *args):
    if x == "+":
        for i in args:
            res_func += i
    elif x == "-":
        for i in args:
            res_func -= i
    elif x == "/":
        for i in args:
            res_func /= i
    else:
        for i in args:
            res_func *= i
    return res_func


