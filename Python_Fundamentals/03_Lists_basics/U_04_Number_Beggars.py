a = input()
ll = [int(i) for i in a.split(', ')]
result = []
beggars = int(input())
n = 0
# fill the result list with number of zeroes = beggars
for _ in range(beggars):
    result.append(0)


while len(ll) > 0:
    number = ll.pop(0)
    result[n] += number
    if n < beggars - 1:
        n += 1
    else:
        n = 0

print(result)