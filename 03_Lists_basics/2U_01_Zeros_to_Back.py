ll = input().split(', ')
for i in range(len(ll)):
    ll[i] = int(ll[i])


for i in range(len(ll)):
    if ll[i] == 0:
        ll.pop(i)
        ll.append(0)
print(ll)
