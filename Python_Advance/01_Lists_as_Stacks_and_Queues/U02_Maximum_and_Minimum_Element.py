number = int(input())
result = []
for _ in range(number):
    command = input().split(' ')
    if command[0] == '1':
        number = int(command[1])
        result.append(number)
    elif command[0] == '2':
        if len(result) > 0:
            result.pop()
    elif command[0] == '3':
        if len(result) > 0:
            print(max(result))
    elif command[0] == '4':
        if len(result) > 0:
            print(min(result))

result = result[::-1]
print(*result, sep=', ')
