targets = input().split(' ')
targets = [int(x) for x in targets]
command = input().split()
while command[0] != 'End':
    if command[0] == 'Shoot':
        shoot_index = int(command[1])
        shoot_power = int(command[2])
        if len(targets) > shoot_index:
            targets[shoot_index] -= shoot_power
            if targets[shoot_index] <= 0:
                targets.pop(shoot_index)

        command = input().split()

    elif command[0] == 'Add':
        add_index = int(command[1])
        add_value = int(command[2])
        if len(targets) >= add_index:
            targets.insert(add_index, add_value)
        else:
            print("Invalid placement!")

        command = input().split()

    elif command[0] == 'Strike':
        strike_index = int(command[1])
        strike_radius = int(command[2])
        if strike_index - strike_radius > 0 and strike_index + strike_radius < len(targets):
            targets = targets[:strike_index - strike_radius] + targets[strike_index + strike_radius + 1:]
        else:
            print("Strike missed!")

        command = input().split()

print(*targets, sep='|')
