x = int(input())
y = int(input())
z = int(input())
available_space = x * y * z
while True:
    command = input()
    if command == 'Done':
        print(f"{available_space} Cubic meters left.")
        break
    number = int(command)
    if available_space >= number:
        available_space -= number
    else:
        print(f'No more free space! You need {number - available_space} Cubic meters more.')
        break
