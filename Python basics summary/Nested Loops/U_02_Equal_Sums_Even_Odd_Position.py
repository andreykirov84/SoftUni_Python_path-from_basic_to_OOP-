x = int(input())
y = int(input())
ll = []
ll_even = []
ll_odd = []
ll_print = []
for i in range(x, y + 1):
    ll = list(map(int, str(i)))
    for j in range(len(ll)):
        if j % 2 == 0:
            ll_odd.append(ll[j])
        else:
            ll_even.append(ll[j])
    if sum(ll_even) == sum(ll_odd):
        ll_print.append(str(i))
    ll_even = []
    ll_odd = []
print(' '.join(ll_print))
