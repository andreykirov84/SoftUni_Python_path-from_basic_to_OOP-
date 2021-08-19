ll = input().split()
result = ''
for word in ll:
    result += word * len(word)
print(result)
