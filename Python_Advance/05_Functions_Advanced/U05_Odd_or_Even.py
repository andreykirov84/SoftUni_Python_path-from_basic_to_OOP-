command = input()
ll = [int(x) for x in input().split(' ')]
result_ll = []
if command == 'Even':
    result_ll = [x for x in ll if x % 2 == 0]
else:
    result_ll = [x for x in ll if x % 2 != 0]
print(f'{sum(result_ll) * len(ll)}')
