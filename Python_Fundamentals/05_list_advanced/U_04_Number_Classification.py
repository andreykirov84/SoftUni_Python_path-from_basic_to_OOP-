ll = list(map(lambda x: int(x), input().split(', ')))
separator = ', '
positive_string = 'Positive: '
positive_ll = [number for number in ll if number >= 0]
positive_string += str(positive_ll[0])
for i in range(1, len(positive_ll)):
    positive_string += separator
    positive_string += str(positive_ll[i])
print(positive_string)

negative_string = 'Negative: '
negative_ll = [number for number in ll if number < 0]
negative_string += str(negative_ll[0])
for i in range(1, len(negative_ll)):
    negative_string += separator
    negative_string += str(negative_ll[i])
print(negative_string)

even_string = 'Even: '
even_ll = [number for number in ll if abs(number) % 2 == 0]
even_string += str(even_ll[0])
for i in range(1, len(even_ll)):
    even_string += separator
    even_string += str(even_ll[i])
print(even_string)

odd_string = 'Odd: '
odd_ll = [number for number in ll if abs(number) % 2 != 0]
odd_string += str(odd_ll[0])
for i in range(1, len(odd_ll)):
    odd_string += separator
    odd_string += str(odd_ll[i])
print(odd_string)


