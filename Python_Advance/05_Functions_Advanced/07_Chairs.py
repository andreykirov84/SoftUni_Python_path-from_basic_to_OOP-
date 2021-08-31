def chair_combination(names, size, result=[]):
    if len(result) == size:
        print(*result, sep=', ')
        return

    for i in range(len(names)):
        name = names[i]
        result.append(name)
        chair_combination(names[i + 1:], size, result)
        result.pop()


names = input().split(', ')
size = int(input())
chair_combination(names, size)
