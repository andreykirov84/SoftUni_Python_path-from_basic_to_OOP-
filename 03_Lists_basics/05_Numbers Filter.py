n = int(input())
ll = []
result = []
for _ in range(n):
    number = int(input())
    ll.append(number)

command = input()
if command == 'even':
    for i in range(len(ll)):
        if ll[i] == 0:
            result.append(ll[i])
        elif ll[i] % 2 == 0:
            result.append(ll[i])

if command == 'odd':
    for i in range(len(ll)):
        if ll[i] != 0:
            if ll[i] % 2 != 0:
                result.append(ll[i])

if command == 'negative':
    for i in range(len(ll)):
        if ll[i] < 0:
            result.append(ll[i])

if command == 'positive':
    for i in range(len(ll)):
        if ll[i] >= 0:
            result.append(ll[i])

print(result)