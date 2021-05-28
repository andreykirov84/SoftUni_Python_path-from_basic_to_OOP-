# function to return key for any value
def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


# Driver Code

test = {"java": 100, "python": 112, "c": 11, "cython": 112}

# print(get_key(test, 100))
# print(get_key(test, 11))


def sorted_by_increased_value(dict):
    return sorted(dict.items(), key=lambda t: t[::-1])

def sorted_by_decreased_value(dict):
    return sorted(dict.items(), key=lambda t: t[::-1], reverse=True)


# print(sorted_by_increased_value(test))
# print(sorted_by_decreased_value(test))

test_ll = [['Pesho', 1, 5], ['Gosho', 10, 2], ['Tosho', 8, 20]]


def sorted_by_increased_value(ll, index):
    return sorted(ll, key=lambda t: t[index])


print(sorted_by_increased_value(test_ll, -1))
print(sorted_by_increased_value(test_ll, 1))


