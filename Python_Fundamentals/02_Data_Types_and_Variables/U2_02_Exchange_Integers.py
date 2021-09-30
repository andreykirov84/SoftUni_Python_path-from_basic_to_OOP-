a = int(input())
b = int(input())
c = 0
print(f'Before:\na = {a}\nb = {b}')

c = a
a = b
b = c

print(f'After:\na = {a}\nb = {b}')
