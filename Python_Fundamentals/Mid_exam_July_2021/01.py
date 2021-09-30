import math

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
total_money_needed = 0

for i in range(1, students + 1):
    if i % 5 != 0:
        total_money_needed += flour_price
    total_money_needed += 10 * egg_price

apron_needed = math.ceil(1.2 * students)
total_money_needed += apron_needed * apron_price

if total_money_needed <= budget:
    print(f'Items purchased for {total_money_needed:.2f}$.')
else:
    print(f'{total_money_needed - budget:.2f}$ more needed.')
