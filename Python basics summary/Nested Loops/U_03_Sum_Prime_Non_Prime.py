number = input()
ll_prime = []
ll_not_prime = []
flag = False
while number != 'stop':
    number = int(number)
    if number < 0:
        print("Number is negative.")
        break
    else:
        for i in range(2, number):
            if number % i == 0:
                flag = True
                break
        if flag:
            ll_not_prime.append(number)
        else:
            ll_prime.append(number)
        number = input()
        flag = False

print(f"Sum of all prime numbers is: {sum(ll_prime)}")
print(f"Sum of all non prime numbers is: {sum(ll_not_prime)}")