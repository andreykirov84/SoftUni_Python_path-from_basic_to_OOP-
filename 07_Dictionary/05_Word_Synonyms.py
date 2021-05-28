synonyms = {}
number = int(input())

while number > 0:
    key = input()
    value = input()
    if key in synonyms:
        synonyms[key] += [value]
    else:
        synonyms[key] = [value]
    number -= 1

for key in synonyms:
    value = synonyms.get(key)
    final_value = f'{value[0]}'
    for i in range(1, len(value)):
        final_value += f', {value[i]}'

    print(f'{key} - {final_value}')
