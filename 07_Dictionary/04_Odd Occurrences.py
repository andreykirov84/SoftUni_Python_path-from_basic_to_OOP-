ll = input().split(' ')
result = {}
for word in ll:
    key = word.lower()
    if key in result:
        result[key] += 1
    else:
        result[key] = 1

final_list = []
for element in result:
    if result.get(element) % 2 != 0:
        final_list.append(element)

print(*final_list)
