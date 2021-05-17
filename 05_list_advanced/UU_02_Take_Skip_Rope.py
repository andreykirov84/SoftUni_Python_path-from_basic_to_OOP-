input_string = input()
number_list = []
non_number_list = []
result = ''
for word in input_string:
    if word.isdigit():
        number_list.append(word)
    else:
        non_number_list.append(word)

[int(x) for x in number_list]

for i in range(0, len(number_list), 2):
    j = i + 1
    if number_list[i] == 0:
        del non_number_list[0:number_list[i + 1]]
    else:
        result += str(non_number_list[:number_list[i]])
        x = number_list[i] + non_number_list[i + 1]
        del non_number_list[0:x]

print(result)
