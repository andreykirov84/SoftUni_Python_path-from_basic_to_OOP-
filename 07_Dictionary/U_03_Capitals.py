""" wihtout using zip() function"""
# country = input().split(', ')
# capitals = input().split(', ')
# for i in range(len(country)):
#     print(f'{country[i]} -> {capitals[i]}')

""" using zip() function and dict comprehension"""
country = input().split(', ')
capitals = input().split(', ')
# ll = list(zip(country, capitals))
# for pair in ll:
#     print(f'{pair[0]} -> {pair[1]}')
result_dict = {k: v for (k, v) in zip(country, capitals)}
for key, value in result_dict.items():
    print(f'{key} -> {value}')
