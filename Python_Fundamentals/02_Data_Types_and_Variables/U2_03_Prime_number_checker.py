number = int(input())
flag = None


if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            flag = False
            break
        else:
            flag = True

print(flag)