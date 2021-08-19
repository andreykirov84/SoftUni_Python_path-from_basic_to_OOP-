command = input()
result = {}
while command != 'stop':
    quantity = int(input())
    if command not in result.keys():
        result.update({command: quantity})
    else:
        value = result.get(command) + quantity
        result.update({command: value})
    command = input()

for key, value in result.items():
    print(f'{key} -> {value}')
