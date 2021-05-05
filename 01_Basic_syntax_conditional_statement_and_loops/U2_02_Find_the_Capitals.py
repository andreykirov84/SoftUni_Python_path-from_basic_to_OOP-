""" Solution 1"""
# import string
#
# all_cap = set(string.ascii_uppercase)
#
#
# ll = list(input())
# result_ll = []
# capital_ll = []
# for i in range(len(ll)):
#     if ll[i] in all_cap:
#         result_ll.append(i)
#
# print(result_ll)


""" Solution 2"""
ll = list(input())
result_ll = []
capital_ll = []
for i in range(len(ll)):
    if 65 <= ord(ll[i]) <= 90:
        result_ll.append(i)

print(result_ll)


