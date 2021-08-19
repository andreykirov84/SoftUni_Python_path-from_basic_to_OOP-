destroyed_ships = 0
number = int(input())
matrix = []
for _ in range(number):
    ll = [int(x) for x in input().split(' ')]
    matrix.append(ll)

commands = input().split(' ')
for i in range(len(commands)):
    sub_ll = [int(x) for x in commands[i].split('-')]

    if matrix[sub_ll[0]][sub_ll[1]] != 0:
        matrix[sub_ll[0]][sub_ll[1]] -= 1
        if matrix[sub_ll[0]][sub_ll[1]] == 0:
            destroyed_ships += 1

print(destroyed_ships)
