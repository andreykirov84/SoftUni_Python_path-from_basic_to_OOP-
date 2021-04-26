# цена на багаж -> зависи от теглото
# оскъпяване на цената -> зависи от броя дни
# обща цена за багажите = цена на багаж * броя на багаж

price_over_20_kg = float(input())
kg = float(input())
days = int(input())
count = int(input())

price_per_one = 0  # тегло
if kg < 10:
    price_per_one = 0.2 * price_over_20_kg
elif 10 <= kg <= 20:
    price_per_one = 0.5 * price_over_20_kg
elif kg > 20:
    price_per_one = price_over_20_kg

# оскъпяване
if days > 30:
    price_per_one = price_per_one + 0.10 * price_per_one
    # price_per_one = 1.1 * price_per_one
elif 7 <= days <= 30:
    price_per_one = price_per_one + 0.15 * price_per_one
    # price_per_one = 1.15 * price_per_one
elif days < 7:
    price_per_one = price_per_one + 0.4 * price_per_one
    # price_per_one = 1.4 * price_per_one

total_price = count * price_per_one
print(f'The total price of bags is: {total_price:.2f} lv.')