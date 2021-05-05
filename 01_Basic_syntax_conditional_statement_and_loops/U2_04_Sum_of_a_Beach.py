def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count


input_string = input().lower()
sand_number = count_substring(input_string, 'sand')
water_number = count_substring(input_string, 'water')
fish_number = count_substring(input_string, 'fish')
sun_number = count_substring(input_string, 'sun')
result = sand_number + water_number + fish_number + sun_number
print(result)
