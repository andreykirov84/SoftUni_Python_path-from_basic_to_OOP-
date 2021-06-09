text = list(input())
digits = ''
letters = ''
rest_char = ''
for char in text:
    if str(char).isdigit():
        digits += str(char)
    elif str(char).isalpha():
        letters += str(char)
    else:
        rest_char += str(char)

print(digits)
print(letters)
print(rest_char)