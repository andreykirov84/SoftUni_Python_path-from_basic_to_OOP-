initial_ll = input().split('!')
command = input()
while command != 'Go Shopping!':
    command = command.split(' ')
    if command[0] == 'Urgent' and command[1] not in initial_ll:
        initial_ll.insert(0, command[1])
    elif command[0] == 'Unnecessary' and command[1] in initial_ll:
        initial_ll.remove(command[1])
    elif command[0] == 'Correct' and command[1] in initial_ll:
        old = command[1]
        new = command[2]
        item_index = initial_ll.index(old)
        initial_ll[item_index] = new
    elif command[0] == 'Rearrange' and command[1] in initial_ll:
        item = command[1]
        initial_ll.remove(item)
        initial_ll.append(item)
    command = input()

print(*initial_ll, sep=', ')
