def repeat(string, number):
    result = ''
    for _ in range(number):
        result += string
    return result


input_string = input()
repeater = int(input())

print(repeat(input_string, repeater))
