ll = []
n2 = 0
n3 = 0
n4 = 0

number = int(input())

for _ in range(number):
    i = int(input())
    ll.append(i)

for i in ll:
    if i % 2 == 0:
        n2 += 1
    if i % 3 == 0:
        n3 += 1
    if i % 4 == 0:
        n4 += 1

p2 = n2 / number * 100
p3 = n3 / number * 100
p4 = n4 / number * 100

print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
