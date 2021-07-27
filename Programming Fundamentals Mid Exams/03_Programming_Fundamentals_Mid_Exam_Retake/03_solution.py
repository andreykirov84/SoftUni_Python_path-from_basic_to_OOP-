ll = input().split(' ')
ll = [int(x) for x in ll]
command = input().split(' ')
while command[0] != 'End':
    if command[0] == 'Shoot' and len(ll) > int(command[1]):
        target_index = int(command[1])
        power = int(command[2])
        ll[target_index] -= power
        if ll[target_index] <= 0:
            ll.pop(target_index)
            command = input().split(' ')
        else:
            command = input().split(' ')

    elif command[0] == 'Add':
        target_index = int(command[1])
        value = int(command[2])
        if len(ll) >= target_index:
            ll.insert(target_index, value)
            command = input().split(' ')
        else:
            print("Invalid placement!")
            command = input().split(' ')

    elif command[0] == 'Strike':
        target_index = int(command[1])
        radius = int(command[2])
        if target_index - radius >= 0 and target_index + radius < len(ll):
            low_border = target_index - radius - 1
            high_border = target_index + radius
            for i in range(high_border, low_border, -1):
                ll.pop(i)
            command = input().split(' ')
        else:
            print("Strike missed!")
            command = input().split(' ')

print(*ll, sep='|')
