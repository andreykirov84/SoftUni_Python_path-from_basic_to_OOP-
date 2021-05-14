ll1 = input().split(', ')
ll2 = input().split(', ')
result = []
for i in range(len(ll1)):
    for j in range(len(ll2)):
        if ll1[i] in ll2[j] and ll1[i] not in result:
            result.append(ll1[i])

print(result)
