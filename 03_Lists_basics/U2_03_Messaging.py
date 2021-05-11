result = ''

ll = input().split(' ')
# for i in range(len(ll)):
#     ll[i] = int(ll[i])

text = list(input())

for i in range(len(ll)):
    x = list(ll[i])
    for j in range(len(x)):
        x[j] = int(x[j])
    number = sum(x)
    if number > len(text):
        index = number % len(text)
    else:
        index = number
    result += text[index]
    text.pop(index)

print(result)


