level = int(input())
rooms = int(input())
floor = []

for i in range(level, 0, -1):
    for j in range(rooms):
        if i == level:
            floor.append(f'L{i}{j}')
            if j == rooms - 1:
                print(' '.join(floor))
                floor = []
        elif i % 2 == 0:
            floor.append(f'O{i}{j}')
            if j == rooms - 1:
                print(' '.join(floor))
                floor = []
        else:
            floor.append(f'A{i}{j}')
            if j == rooms - 1:
                print(' '.join(floor))
                floor = []
