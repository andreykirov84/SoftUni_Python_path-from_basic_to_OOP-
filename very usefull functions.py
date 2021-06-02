""" sort dictionary by increased value (by def), or by decreased value if decreased = True. If we have 2 equal values
they will be sorted also by key (alphabetically) if equal_alphabetic_sort=True (by def)"""


def sort_dict_by_value(dict, decreased=False, equal_alphabetic_sort=True):
    dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=decreased)}
    value_key_pairs = ((value, key) for (key, value) in dict.items())
    sorted_value_key_pairs = sorted(value_key_pairs, reverse=decreased)
    if equal_alphabetic_sort:
        for i in range(0, len(sorted_value_key_pairs) - 1):
            if sorted_value_key_pairs[i][1] > sorted_value_key_pairs[i + 1][1]:
                sorted_value_key_pairs[i], sorted_value_key_pairs[i + 1] = sorted_value_key_pairs[i + 1], \
                                                                           sorted_value_key_pairs[i]
    return {k: v for v, k in sorted_value_key_pairs}


""" Returns only the keys after the dict is sorted by decreased values"""
def keys_dict_sorted_by_decrease_value(dict):
    return sorted(dict, key=lambda k: (-dict[k], k))


""" returns a sorted by key dictionary"""
def sorted_by_key(dict):
    return {k: v for k, v in sorted(dict.items(), key=lambda keys: keys[0])}

# function testing
dict = {"Math": 34, "Science": 12, "English": 89, "Physics": 8, "Anglish": 89, "Pesho": 0}

print(dict)
# -> {'Math': 34, 'Science': 12, 'English': 89, 'Physics': 8, 'Anglish': 89, 'Pesho': 0}

print(sort_dict_by_value(dict))
# -> {'Pesho': 0, 'Physics': 8, 'Math': 34, 'Anglish': 89, 'English': 89, 'Science': 12}

print(sort_dict_by_value(dict, decreased=True))
# -> {'Anglish': 89, 'English': 89, 'Math': 34, 'Physics': 8, 'Pesho': 0, 'Science': 12}

print({k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)})
# -> {'English': 89, 'Anglish': 89, 'Math': 34, 'Science': 12, 'Physics': 8, 'Pesho': 0}

print(keys_dict_sorted_by_decrease_value(dict))
# -> ['Anglish', 'English', 'Math', 'Science', 'Physics', 'Pesho']

print(sorted_by_key(dict))
# -> {'Anglish': 89, 'English': 89, 'Math': 34, 'Pesho': 0, 'Physics': 8, 'Science': 12}
