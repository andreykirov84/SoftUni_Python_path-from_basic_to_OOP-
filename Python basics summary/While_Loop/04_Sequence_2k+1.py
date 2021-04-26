number = int(input())
ll = [1]
while ll[-1] <= number:
    i = ll[-1]
    j = 2 * i + 1
    if j <= number:
        ll.append(j)
    else:
        break
for i in range(len(ll)):
    print(ll[i])

