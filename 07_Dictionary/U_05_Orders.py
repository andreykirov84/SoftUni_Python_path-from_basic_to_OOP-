command = input()
stock = {}
while command != 'buy':
    command = command.split(' ')
    name = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if name in stock:
        old_quantity = stock.get(name)[1]
        stock.update({name: [price, old_quantity + quantity]})
    else:
        stock.update({name: [price, quantity]})
    command = input()

[print(f'{key} -> {value[0] * value[1]:.2f}') for key, value in stock.items()]
