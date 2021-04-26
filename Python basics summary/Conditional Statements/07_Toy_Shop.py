puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2
discount_threshold = 50
discount = 0.25
rent = 0.1
trip_price = float(input())
puzzle_amount = int(input())
talking_doll_amount = int(input())
teddy_bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())
total_amount = puzzle_amount + talking_doll_amount + teddy_bear_amount + minion_amount + truck_amount
total_income = puzzle_amount * puzzle_price + talking_doll_amount * talking_doll_price + teddy_bear_amount * teddy_bear_price + minion_amount * minion_price + truck_amount * truck_price
if total_amount >= discount_threshold:
    total_income -= total_income * discount
    total_income -= total_income * rent
else:
    total_income -= total_income * rent

if total_income >= trip_price:
    money_left = total_income - trip_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_left = trip_price - total_income
    print(f"Not enough money! {money_left:.2f} lv needed.")
