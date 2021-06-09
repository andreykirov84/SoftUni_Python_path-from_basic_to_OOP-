text = input()
final_text = ''
for char in text:
    new_char = chr(ord(char) + 3)
    final_text += new_char

print(final_text)
