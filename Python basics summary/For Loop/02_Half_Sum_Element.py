number = int(input())
ll = []
for _ in range(number):
    i = int(input())
    ll.append(i)
is_not_sum = True
for i in ll:
    if i == sum(ll) - i:
        is_not_sum = False
        print(f'Yes\nSum = {i}')
        break

if is_not_sum:
    print(f'No\nDiff = {abs(max(ll) - sum(ll) + max(ll))}')
