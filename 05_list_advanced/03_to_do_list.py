result = [0] * 10
command = input()
ll2 = []
while command != 'End':
    ll = command.split('-')
    index = int(ll[0]) - 1
    result[index] = ll[1]
    command = input()

for i in range(10):
    if result[i] != 0:
        ll2.append(result[i])


print(ll2)

