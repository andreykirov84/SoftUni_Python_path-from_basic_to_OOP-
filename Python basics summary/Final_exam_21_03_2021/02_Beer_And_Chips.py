import math

price_beer = 1.20


name = input()
budget = float(input())
beer_quantity = int(input())
chips_quantity = int(input())

total_price_beer = price_beer * beer_quantity
price_chips = 0.45 * total_price_beer
total_price_chips = math.ceil(chips_quantity * price_chips)
total_price = total_price_chips + total_price_beer

if budget >= total_price:
    print(f'{name} bought a snack and has {budget - total_price:.2f} leva left.')
else:
    print(f"{name} needs {total_price - budget:.2f} more leva!")
