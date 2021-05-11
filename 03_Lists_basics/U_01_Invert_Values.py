a = input()
ll = [int(i) for i in a.split(' ')]

result = []

for i in range(len(ll)):
    reverse_number = ll[i] - (2 * ll[i])
    result.append(reverse_number)

print(result)


