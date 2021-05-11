a = input()
number = int(input())
ll = a.split(' ')
n = int(len(ll) / 2)

for _ in range(number):
    ll1 = ll[:n]
    ll2 = ll[n:]
    result = []
    for i in range(len(ll1)):
        result.append(ll1[i])
        result.append(ll2[i])
    ll = result
    
print(ll)


