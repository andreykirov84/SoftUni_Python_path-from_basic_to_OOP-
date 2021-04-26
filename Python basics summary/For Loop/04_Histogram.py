number = int(input())
ll1 = []
ll2 = []
ll3 = []
ll4 = []
ll5 = []
for _ in range(number):
    i = int(input())
    if i < 200:
        ll1.append(i)
    elif 199 < i <= 399:
        ll2.append(i)
    elif 399 < i <= 599:
        ll3.append(i)
    elif 599 < i <= 799:
        ll4.append(i)
    else:
        ll5.append(i)
p1 = len(ll1) / number * 100
p2 = len(ll2) / number * 100
p3 = len(ll3) / number * 100
p4 = len(ll4) / number * 100
p5 = len(ll5) / number * 100
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
