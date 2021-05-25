elements = input().split(' ')
bakery = {}
for i in range(0, len(elements), 2):
    bakery[elements[i]] = int(elements[i + 1])
print(bakery)
