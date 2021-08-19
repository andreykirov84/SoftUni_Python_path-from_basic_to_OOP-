ll = input().split(' ')
palindrome = input()
counter = 0
for i in range(len(ll)):
    if ll[i] == palindrome:
        counter += 1

result = []
for i in range(len(ll)):
    x = ll[i]
    if x == x[::-1]:
        result.append(x)

print(result)
print(f'Found palindrome {counter} times')
