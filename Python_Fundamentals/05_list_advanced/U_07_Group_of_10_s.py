ll = list(map(lambda x: int(x), input().split(', ')))
groups = max(ll) // 10 + 1
result = []

for i in range(groups):
    max_number = 10 + i * 10
    min_number = 1 + i * 10
    temp_ll = []
    for number in ll:
        if min_number <= number <= max_number:
            temp_ll.append(number)
    result.append(temp_ll)

if len(result[-1]) == 0:
    result.pop()

for i in range(len(result)):
    print(f"Group of {10 + i * 10}'s: {result[i]}")


