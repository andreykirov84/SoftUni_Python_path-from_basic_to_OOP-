inventory = input(). split(', ')
command = input()
while command != 'Craft!':
    command = command.split(' - ')
    if len(command) != 2:
        command = input()

    elif command[0] == 'Collect':
        if command[1] not in inventory:
            inventory.append(command[1])
        command = input()

    elif command[0] == 'Drop':
        if command[1] in inventory:
            inventory.remove(command[1])
        command = input()

    elif command[0] == 'Combine Items':
        items = command[1].split(':')
        old_item = items[0]
        new_item = items[1]
        if old_item in inventory:
            item_index = inventory.index(old_item)
            inventory.insert(item_index + 1, new_item)
        command = input()

    elif command[0] == 'Renew':
        if command[1] in inventory:
            inventory.remove(command[1])
            inventory.append(command[1])
        command = input()

    else:
        command = input()

print(*inventory, sep=', ')
