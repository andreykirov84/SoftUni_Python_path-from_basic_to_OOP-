divisor = int(input())
bound = int(input())
result = 0
for i in range(divisor, bound + 1):
    if i % divisor == 0 and i > result:
        result = i
print(result)
