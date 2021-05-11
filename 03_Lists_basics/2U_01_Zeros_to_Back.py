ll = input().split(', ')
for i in range(len(ll)):
    ll[i] = int(ll[i])

ll2 = []

for i in range(len(ll)):
    if ll[i] != 0:
        ll2.append(ll[i])

for _ in range(len(ll) - len(ll2)):
    ll2.append(0)

print(ll2)
