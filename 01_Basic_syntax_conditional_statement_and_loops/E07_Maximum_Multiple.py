devisor = int(input())
bound = int(input())
number = bound
while number % devisor != 0:
    number -= 1
print(number)