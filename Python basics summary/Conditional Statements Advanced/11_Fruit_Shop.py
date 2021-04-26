working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']
fruits_price_week = {
    'banana': 2.50,
    'apple': 1.20,
    'orange': 0.85,
    'grapefruit': 1.45,
    'kiwi': 2.70,
    'pineapple': 5.50,
    'grapes': 3.85
    }
fruits_price_weekend = {
    'banana': 2.70,
    'apple': 1.25,
    'orange': 0.90,
    'grapefruit': 1.60,
    'kiwi': 3.00,
    'pineapple': 5.60,
    'grapes': 4.20
    }

fruit = input()
day = input()
quantity = float(input())


def valid_day(date):
    if date in working_days or date in weekend:
        return True


if fruit in fruits_price_week.keys() and valid_day(day):
    if day in working_days:
        print(f'{fruits_price_week[fruit] * quantity:.2f}')
    elif day in weekend:
        print(f'{fruits_price_weekend[fruit] * quantity:.2f}')
else:
    print("error")

