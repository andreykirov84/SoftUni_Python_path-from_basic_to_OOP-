capacity = 0
max_capacity = 255
n = int(input())
for _ in range(n):
    water = int(input())
    if max_capacity >= capacity + water:
        capacity += water
    else:
        print('Insufficient capacity!')
print(capacity)
