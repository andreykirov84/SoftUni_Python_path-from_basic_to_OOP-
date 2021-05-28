storage = {}
command = input()

while command != 'statistics':
    elements = command.split(': ')
    key = elements[0]
    value = int(elements[1])
    if key in storage:
        storage[key] += value
    else:
        storage[key] = value
    command = input()

total_products = 0
total_quantity = 0
result = 'Products in stock:\n'
for product in storage:
    result += f'- {product}: {storage.get(product)}\n'
    total_products += 1
    total_quantity += storage.get(product)

print(result, end='')
print(f'Total Products: {total_products}')
print(f'Total Quantity: {total_quantity}')




