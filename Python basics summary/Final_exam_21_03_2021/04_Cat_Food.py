food_price_per_kg = 12.45
cats = int(input())
group_one = 0
group_two = 0
group_three = 0
total_food_quantity = 0

for _ in range(cats):
    food_quantity = float(input())
    if 100 <= food_quantity < 200:
        group_one += 1
    elif 200 <= food_quantity < 300:
        group_two += 1
    elif 300 <= food_quantity < 400:
        group_three += 1
    total_food_quantity += food_quantity

total_price = total_food_quantity / 1000 * food_price_per_kg

print(f"Group 1: {group_one} cats.")
print(f"Group 2: {group_two} cats.")
print(f"Group 3: {group_three} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")

