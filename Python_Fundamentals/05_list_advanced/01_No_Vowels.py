vowels = ['a', 'o', 'u', 'e', 'i']
ll = list(input())
result = []
for i in range(len(ll)):
    if ll[i] not in vowels:
        result.append(ll[i])

for i in result:
    print(i, end='')
