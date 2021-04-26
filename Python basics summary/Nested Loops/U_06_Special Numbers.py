number = int(input())
ll = []
ll_final = []
flag = False
for i in range(1111, 10000):
    ll = list(str(i))
    for j in ll:
        if int(j) != 0:
            if number % int(j) != 0:
                flag = True
                break
        else:
            flag = True
    if not flag:
        ll_final.append(str(i))
    flag = False
    ll = []
print(' '.join(ll_final))
