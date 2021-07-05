energy = int(input())
wins = 0
command = input()
flag = False
while command != "End of battle":
    distance = int(command)
    if energy >= distance:
        wins += 1
        energy -= distance
        if wins % 3 == 0:
            energy += wins
        command = input()
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        flag = True
        break

if not flag:
    print(f"Won battles: {wins}. Energy left: {energy}")
