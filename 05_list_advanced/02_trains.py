number = int(input())
ll = []
for _ in range(number):
    ll.append(0)

command = input()
while command != 'End':
    command_list = command.split(' ')
    if command_list[0] == 'add':
        ll[-1] += int(command_list[1])
    elif command_list[0] == 'insert':
        index = int(command_list[1])
        ll[index] += int(command_list[2])
    elif command_list[0] == 'leave':
        index = int(command_list[1])
        ll[index] -= int(command_list[2])
    command = input()

print(ll)