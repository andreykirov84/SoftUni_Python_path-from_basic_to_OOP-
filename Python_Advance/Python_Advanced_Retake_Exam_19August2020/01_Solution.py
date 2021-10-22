customers = [int(x) for x in input().split(', ')]
taxis = [int(x) for x in input().split(', ')]

total_time = 0

while customers and taxis:
    customer = customers[0]
    taxi = taxis[-1]
    if taxi >= customer:
        total_time += customers.pop(0)
        taxis.pop(-1)
    else:
        taxis.pop(-1)

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')

else:
    print('Not all customers were driven to their destinations')
    print('Customers left: ', end='')
    print(*customers, sep=', ')
