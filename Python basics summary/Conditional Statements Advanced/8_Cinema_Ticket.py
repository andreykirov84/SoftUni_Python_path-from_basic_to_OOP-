days_one = ['Monday', 'Tuesday', 'Friday']
days_two = ['Wednesday', 'Thursday']
days_three = ['Saturday', 'Sunday']
price_one = 12
price_two = 14
price_three = 16
day = input()
if day in days_one:
    print(price_one)
elif day in days_two:
    print(price_two)
elif day in days_three:
    print(price_three)

