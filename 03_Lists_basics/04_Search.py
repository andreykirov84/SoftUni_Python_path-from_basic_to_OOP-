n = int(input())
word = input()
full_ll = []
filter_ll = []
for _ in range(n):
    a = input()
    full_ll.append(a)
    if word in a:
        filter_ll.append(a)

print(full_ll)
print(filter_ll)
