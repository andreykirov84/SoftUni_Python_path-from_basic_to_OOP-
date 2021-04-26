commissions_rate = {
    'Sofia': [0.05, 0.07, 0.08, 0.12],
    'Varna': [0.045, 0.075, 0.1, 0.13],
    'Plovdiv': [0.055, 0.08, 0.12, 0.145],
    }
index = None
city = input()
money = float(input())
if city in commissions_rate.keys() and money > 0:
    if 0 < money <= 500:
        index = 0
    elif 500 < money <= 1000:
        index = 1
    elif 1000 < money <= 10000:
        index = 2
    elif money > 10000:
        index = 3
    result = commissions_rate[city][index]
    print(f'{money * result:.2f}')
else:
    print('error')
