def multiplication_sign(*args):
    if 0 in args:
        return 'zero'
    else:
        negative = 0
        for i in range(len(args)):
            if args[i] < 0:
                negative += 1
        if negative % 2 == 0:
            return 'positive'
        else:
            return 'negative'


print(multiplication_sign(float(input()), float(input()), float(input())))
