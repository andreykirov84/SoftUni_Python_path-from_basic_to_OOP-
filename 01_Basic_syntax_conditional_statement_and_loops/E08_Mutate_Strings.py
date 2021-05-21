def list_to_string(ll):
    res_str = ""
    return res_str.join(ll)


string_one = list(input())
string_two = list(input())
all_strings = [list_to_string(string_one)]
for i in range(len(string_one)):
    string_one[i] = string_two[i]
    if list_to_string(string_one) not in all_strings:
        print(list_to_string(string_one))
        all_strings.append(list_to_string(string_one))

