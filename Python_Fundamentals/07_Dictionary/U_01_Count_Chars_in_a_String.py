text = list(input())
result = {}
while ' ' in text:
    text.remove(' ')


for char in text:
    if char in result.keys():
        result.update({char: result.get(char) + 1})
    else:
        result.update({char: 1})

for key, value in result.items():
    print(f'{key} -> {value}')
