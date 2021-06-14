neighborhood = [int(x) for x in input().split("@")]
default_index = 0
while True:
    command = input()
    if command == "Love!":
        print(f"Cupid's last position was {default_index}.")
        if neighborhood.count(0) < len(neighborhood):
            print(f"Cupid has failed {len(neighborhood)- neighborhood.count(0)} places.")
        else:
            print("Mission was successful.")
        break
    command = command.split()
    default_index += int(command[1])
    if default_index > len(neighborhood)-1:
        default_index = 0
    if neighborhood[default_index] == 0:
        print(f"Place {default_index} already had Valentine's day.")
    else:
        neighborhood[default_index] -= 2
        if neighborhood[default_index] == 0:
            print(f"Place {default_index} has Valentine's day.")




