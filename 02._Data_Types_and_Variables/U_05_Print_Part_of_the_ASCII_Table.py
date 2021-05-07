a = int(input())
b = int(input())
c = ''
separator = ' '
for i in range(a, b + 1):
    d = chr(i)
    c += separator + d

print(c)
