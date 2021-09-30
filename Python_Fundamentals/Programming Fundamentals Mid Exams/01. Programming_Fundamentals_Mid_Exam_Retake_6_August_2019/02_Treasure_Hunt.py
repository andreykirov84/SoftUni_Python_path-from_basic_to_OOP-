storage = input().split('|')
command = input().split()
stolen = []

while command[0] != 'Yohoho!':
    if command[0] == 'Loot':
        command.pop(0)
        for item in command:
            if item not in storage:
                storage.insert(0, item)
        command = input().split()

    elif command[0] == 'Drop':
        item_index = int(command[1])
        if len(storage) > item_index:
            item = storage.pop(item_index)
            storage.append(item)
        command = input().split()

    elif command[0] == 'Steal':
        count = int(command[1])
        if count >= len(storage):
            count = len(storage)

        for _ in range(count):
            stolen.append(storage.pop())
        command = input().split()

if len(storage) > 0:
    storage_total_length = 0
    for item in storage:
        storage_total_length += len(item)

    average_treasure_gain = storage_total_length / len(storage)
    stolen = stolen[::-1]
    print(*stolen, sep=', ')
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")

else:
    stolen = stolen[::-1]
    print(*stolen, sep=', ')
    print("Failed treasure hunt.")
