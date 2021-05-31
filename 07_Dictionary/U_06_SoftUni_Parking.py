cars = {}
for _ in range(int(input())):
    command = input().split(' ')
    if command[0] == 'register':
        if command[1] in cars:
            print(f"ERROR: already registered with plate number {cars.get(command[1])}")
        else:
            cars.update({command[1]: command[2]})
            print(f"{command[1]} registered {command[2]} successfully")

    if command[0] == 'unregister':
        if command[1] not in cars:
            print(f"ERROR: user {command[1]} not found")
        else:
            print(f"{command[1]} unregistered successfully")
            cars.pop(command[1])

[print(f'{name} => {number}') for name, number in cars.items()]
