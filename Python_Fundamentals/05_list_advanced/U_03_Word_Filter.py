ll = input().split(' ')
""" turn for loop in list comprehension"""
# for word in ll:
#     if len(word) % 2 == 0:
#         print(word)

# result = [word for word in ll if len(word) % 2 == 0]

[print(word) for word in ll if len(word) % 2 == 0]
