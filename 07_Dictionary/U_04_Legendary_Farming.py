materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
KEY_MATERIAL_LIMIT = 250
is_obtained = False

while True:
    list_of_materials = input().lower().split()
    length = len(list_of_materials)

    for i in range(0, length, 2):
        material = list_of_materials[i + 1]
        quantity = int(list_of_materials[i])

        if material == "shards":
            materials[material] += quantity

            if materials[material] >= KEY_MATERIAL_LIMIT:
                materials[material] -= KEY_MATERIAL_LIMIT
                print("Shadowmourne obtained!")
                is_obtained = True
                break

        elif material == "fragments":
            materials[material] += quantity

            if materials[material] >= KEY_MATERIAL_LIMIT:
                materials[material] -= KEY_MATERIAL_LIMIT
                print("Valanyr obtained!")
                is_obtained = True
                break

        elif material == "motes":
            materials[material] += quantity

            if materials[material] >= KEY_MATERIAL_LIMIT:
                materials[material] -= KEY_MATERIAL_LIMIT
                print("Dragonwrath obtained!")
                is_obtained = True
                break

        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

    if is_obtained:
        break

sorted_key_materials = dict(sorted(materials.items(), key=lambda x: (-x[1], x[0])))
for key, value in sorted_key_materials.items():
    print(f"{key}: {value}")

sorted_junk_materials = dict(sorted(junk.items(), key=lambda x: x[0]))
for junk, value in sorted_junk_materials.items():
    print(f"{junk}: {value}")



# """ sort dictionary by increased value (by def), or by decreased value if decreased = True. If we have 2 equal values
# they will be sorted also by key (alphabetically) if equal_alphabetic_sort=True (by def)"""
#
#
# def sort_dict_by_value(dict, decreased=False, equal_alphabetic_sort=True):
#     value_key_pairs = ((value, key) for (key, value) in dict.items())
#     sorted_value_key_pairs = sorted(value_key_pairs, reverse=decreased)
#     if equal_alphabetic_sort:
#         for i in range(0, len(sorted_value_key_pairs) - 1):
#             if sorted_value_key_pairs[i][1] > sorted_value_key_pairs[i + 1][1]:
#                 sorted_value_key_pairs[i], sorted_value_key_pairs[i + 1] = sorted_value_key_pairs[i + 1], \
#                                                                            sorted_value_key_pairs[i]
#     return {k: v for v, k in sorted_value_key_pairs}
#
#
# def sorted_by_key(dict):
#     return {k: v for k, v in sorted(dict.items(), key=lambda keys: keys[0])}
#
#
# def keys_dict_sorted_by_decrease_value(dict):
#     return sorted(dict, key=lambda k: (-dict[k], k))
#
#
# ll = input().lower().split(' ')
#
# # ll = []
# # line = input()
# # while line != '':
# #     line_ll = line.split(' ')
# #     ll.extend(line_ll)
# #     line = input()
#
#
# key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
# junk = {}
# legendary_item_obtained = None
# for i in range(0, len(ll), 2):
#     key = ll[i + 1].lower()
#     value = int(ll[i])
#     if key == 'shards' or key == 'fragments' or key == 'motes':
#         if key in key_materials.keys():
#             old_value = key_materials.get(key)
#             key_materials.update({key: old_value + value})
#         else:
#             key_materials.update({key: value})
#         if key_materials.get('shards') >= 250 and legendary_item_obtained is None:
#             legendary_item_obtained = 'Shadowmourne'
#             key_materials.update({'shards': key_materials.get('shards') - 250})
#             break
#         elif key_materials.get('fragments') >= 250 and legendary_item_obtained is None:
#             legendary_item_obtained = 'Valanyr'
#             key_materials.update({'fragments': key_materials.get('fragments') - 250})
#             break
#         elif key_materials.get('motes') >= 250 and legendary_item_obtained is None:
#             legendary_item_obtained = 'Dragonwrath'
#             key_materials.update({'motes': key_materials.get('motes') - 250})
#             break
#     else:
#         if key in junk.keys():
#             old_value = junk.get(key)
#             junk.update({key: old_value + value})
#         else:
#             junk.update({key: value})
#
# print(f'{legendary_item_obtained} obtained!')
# # key_materials = sort_dict_by_value(key_materials, decreased=True)
# key_materials_sorted_keys = keys_dict_sorted_by_decrease_value(key_materials)
#
# final_key_materials = {}
# for key in key_materials_sorted_keys:
#     material_value = key_materials.get(key)
#     final_key_materials.update({key: material_value})
#
# junk = sorted_by_key(junk)
#
# [print(f'{key}: {value}') for key, value in final_key_materials.items()]
# [print(f'{key}: {value}') for key, value in junk.items()]
#
