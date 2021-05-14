ll = list(map(lambda x: int(x), input().split('.')))
if ll[2] == 9:
    if ll[1] == 9:
        ll[0] += 1
        ll[1] = 0
        ll[2] = 0
    else:
        ll[1] += 1
        ll[2] = 0
else:
    ll[2] += 1


for i in range(len(ll) - 1):
    print(ll[i], end='.')
print(ll[-1])

