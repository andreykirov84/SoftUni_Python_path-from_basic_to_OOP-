input_number = int(input())
base = int(input())
ll = []
result = 0

while input_number != 0:
    ll.append(input_number % 2)
    input_number //= 2

for i in ll:
    if i == base:
        result += 1
# print(ll[::-1])
print(result)
