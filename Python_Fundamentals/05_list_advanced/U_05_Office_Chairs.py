chairs_left = 0
flag = False
for i in range(1, int(input()) + 1):
    ll = input().split(' ')
    room_chairs = len(ll[0])
    needed_chairs = int(ll[1])
    if needed_chairs <= room_chairs:
        chairs_left += room_chairs - needed_chairs
    else:
        flag = True
        print(f'{needed_chairs - room_chairs} more chairs needed in room {i}')


if not flag:
    print(f'Game On, {chairs_left} free chairs left')
