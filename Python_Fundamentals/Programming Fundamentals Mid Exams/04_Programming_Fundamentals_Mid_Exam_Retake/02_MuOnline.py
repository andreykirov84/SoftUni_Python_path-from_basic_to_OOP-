health = 100
bitcoins = 0
room = 0
command_list = list(input().split('|'))
for sub_ll in command_list:
    command = sub_ll.split(' ')
    name = command[0]
    number = int(command[1])
    if name == 'potion':
        health += number
        health_amount = number
        room += 1
        if health > 100:
            health_amount = number - (health - 100)
            health = 100

        print(f'You healed for {health_amount} hp.')
        print(f'Current health: {health} hp.')

    elif name == 'chest':
        bitcoins += number
        room += 1
        print(f"You found {number} bitcoins.")

    else:
        room += 1
        health -= number
        if health <= 0:
            print(f"You died! Killed by {name}.")
            print(f"Best room: {room}")
            break
        else:
            print(f"You slayed {name}.")


if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")

