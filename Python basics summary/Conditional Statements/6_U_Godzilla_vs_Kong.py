budget = float(input())
statist_amount = int(input())
statist_price = float(input())
dekor = budget * 0.1
if statist_amount > 150:
    statist_price *= 0.9
statist_budget = statist_amount * statist_price
money_left = budget - statist_budget - dekor
if money_left >= 0:
    print('Action!')
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_left):.2f} leva more.")
