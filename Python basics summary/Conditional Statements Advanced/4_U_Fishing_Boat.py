budget = int(input())
season = input()
fisherman_number = int(input())
price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
else:
    price = 2600

if fisherman_number <= 6:
    price = price * 0.9
elif 6 < fisherman_number <= 11:
    price = price * 0.85
elif fisherman_number > 11:
    price = price * 0.75

if fisherman_number % 2 == 0 and season != 'Autumn':
    price = price * 0.95

if price <= budget:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
