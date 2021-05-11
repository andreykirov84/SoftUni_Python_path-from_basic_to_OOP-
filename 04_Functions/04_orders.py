def order(product, quantity):
    total_sum = 0
    if product == 'coffee':
        total_sum = quantity * 1.50
    elif product == 'water':
        total_sum = quantity * 1.00
    elif product == 'coke':
        total_sum = quantity * 1.40
    elif product == 'snacks':
        total_sum = quantity * 2
    return total_sum


product = input()
quantity = int(input())
x = order(product, quantity)
print(f'{x:.2f}')
