"""
Type	Maximum Price
Clothes	50.00
Shoes	35.00
Accessories	20.50

"""
result = []
profit = 0
final_sum = 0
items = input().split('|')
budget = float(input())
for i in range(len(items)):
    ll = items[i].split('->')
    if ll[0] == 'Clothes' and float(ll[1]) <= 50 and budget >= float(ll[1]):
        budget -= float(ll[1])
        result.append(1.4 * float(ll[1]))
        profit += 0.4 * float(ll[1])

    elif ll[0] == 'Shoes' and float(ll[1]) <= 35 and budget >= float(ll[1]):
        budget -= float(ll[1])
        result.append(1.4 * float(ll[1]))
        profit += 0.4 * float(ll[1])

    elif ll[0] == 'Accessories' and float(ll[1]) <= 20.50 and budget >= float(ll[1]):
        budget -= float(ll[1])
        result.append(1.4 * float(ll[1]))
        profit += 0.4 * float(ll[1])

final_sum = budget + sum(result)

for i in result:
    print(f"{round(i, 2):.2f}", end=' ')

print(f'\nProfit: {round(profit, 2):.2f}')

if final_sum >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
