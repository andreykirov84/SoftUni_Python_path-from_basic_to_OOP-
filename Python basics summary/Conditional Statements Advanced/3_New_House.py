ROSE = 5
DALIA = 3.80
LALE = 2.80
NARCIS = 3
GLADIOLA = 2.50
flower_price = 0

flower = input()
quantity = int(input())
budget = float(input())
if flower == 'Roses':
    if quantity > 80:
        flower_price = ROSE * 0.9
    else:
        flower_price = ROSE

if flower == 'Dahlias':
    if quantity > 90:
        flower_price = DALIA * 0.85
    else:
        flower_price = DALIA

if flower == 'Tulips':
    if quantity > 80:
        flower_price = LALE * 0.85
    else:
        flower_price = LALE

if flower == 'Narcissus':
    if quantity < 120:
        flower_price = NARCIS * 1.15
    else:
        flower_price = NARCIS

if flower == 'Gladiolus':
    if quantity < 80:
        flower_price = GLADIOLA * 1.20
    else:
        flower_price = GLADIOLA

total_price = flower_price * quantity
if total_price <= budget:
    print(f"Hey, you have a great garden with {quantity} {flower} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")