numbers = list(map(lambda x: int(x), input().split(' ')))
number = int(input())
counter = 0

for i in range(len(numbers)):
    numbers[i] = numbers[i] * number

for j in numbers:
    if j >= sum(numbers) / len(numbers):
        counter += 1

print(f'Score: {counter}/{len(numbers)}. ', end='')
if counter >= len(numbers) / 2:
    print('Employees are happy!')
else:
    print('Employees are not happy!')
