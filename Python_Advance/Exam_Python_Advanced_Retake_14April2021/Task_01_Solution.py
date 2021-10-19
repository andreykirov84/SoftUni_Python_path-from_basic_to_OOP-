first_input_line = input().split(', ')
if first_input_line:
    orders = [int(x) for x in first_input_line]
else:
    orders = []

second_input_line = input().split(', ')
if second_input_line:
    employees = [int(x) for x in second_input_line]
else:
    employees = []

total_pizza_count = 0

for i in range(len(orders) - 1, -1, -1):
    if orders[i] > 10 or orders[i] <= 0:
        orders.pop(i)

while employees and orders:
    # check for negative values and zero and if the orders are in range 1-10 inclusive
    if employees[-1] <= 0:
        employees.pop(-1)
    elif orders[0] <= 0 or orders[0] > 10:
        orders.pop(0)
    else:
        if orders[0] <= employees[-1]:
            total_pizza_count += orders.pop(0)
            employees.pop(-1)

        elif orders[0] > employees[-1]:
            made_by_employee = employees.pop(-1)
            order_left = orders[0] - made_by_employee
            orders[0] = order_left
            total_pizza_count += made_by_employee


if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza_count}')
    print('Employees: ', end='')
    print(*employees, sep=', ')
else:
    print('Not all orders are completed.')
    print('Orders left: ', end='')
    print(*orders, sep=', ')
