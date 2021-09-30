char_ll = input().split(', ')
result_dict = {}
for char in char_ll:
    result_dict.update({char: ord(char)})
print(result_dict)
