def even_odd(*args):
    ll = [int(x) for x in args[:len(args) - 1]]
    command = args[-1]
    if command == 'even':
        result = [x for x in ll if x % 2 == 0]
    else:
        result = [x for x in ll if x % 2 != 0]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
