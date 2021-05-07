a = 97
# b = 122
number = int(input())
for i in range(a, a + number):
    for j in range(a, a + number):
        for k in range(a, a + number):
            print(f'{chr(i)}{chr(j)}{chr(k)}')

