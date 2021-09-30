def genrange(start, stop):
    current_num = start
    while current_num <= stop:
        yield current_num
        current_num += 1


print(list(genrange(1, 10)))