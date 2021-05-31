# # function to return key for any value
# def get_key(my_dict, val):
#     for key, value in my_dict.items():
#         if val == value:
#             return key
#
#     return "key doesn't exist"
#
#
# # Driver Code
#
# test = {"java": 100, "python": 112, "c": 11, "cython": 112}
#
# # print(get_key(test, 100))
# # print(get_key(test, 11))
#
#
# def sorted_by_increased_value(dict):
#     return sorted(dict.items(), key=lambda t: t[::-1])
#
#
# def sorted_by_decreased_value(dict):
#     return sorted(dict.items(), key=lambda t: t[::-1], reverse=True)
#
#
# # print(sorted_by_increased_value(test))
# # print(sorted_by_decreased_value(test))
#
# test_ll = [['Pesho', 1, 5], ['Gosho', 10, 2], ['Tosho', 8, 20]]
#
#
# def sorted_by_increased_value_index(ll, index):
#     return sorted(ll, key=lambda t: t[index])
#
#
# print(sorted_by_increased_value_index(test_ll, -1))
# print(sorted_by_increased_value_index(test_ll, 1))
#
#
dict = { "Math": 34, "Science": 12, "English": 89, "Physics": 8 }
print(dict)
# {'Math': 34, 'Science': 12, 'English': 89, 'Physics': 8}
value_key_pairs = ((value, key) for (key,value) in dict.items())
sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
print(sorted_value_key_pairs)
# [(89, 'English'), (34, 'Math'), (12, 'Science'), (8, 'Physics')]
print({k: v for v, k in sorted_value_key_pairs})
# {'English': 89, 'Math': 34, 'Science': 12, 'Physics': 8}