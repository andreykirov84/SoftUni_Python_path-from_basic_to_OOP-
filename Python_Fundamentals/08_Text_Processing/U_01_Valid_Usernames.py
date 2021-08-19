def correct_check(text):
    final = True
    for char in text:
        result = False
        if char.isalnum():
            result = True
        elif char == '-':
            result = True
        elif char == '_':
            result = True
        if not result:
            final = False
            break
    return final


password_ll = input().split(', ')
valid_ll = []
for word in password_ll:
    if 3 <= len(word) <= 16 and len(word) == len(word.strip()) and correct_check(word):
        valid_ll.append(word)

print(*valid_ll, sep='\n')
