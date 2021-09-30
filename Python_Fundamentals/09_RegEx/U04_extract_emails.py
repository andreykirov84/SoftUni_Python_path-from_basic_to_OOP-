import re


pattern = r'(^|\s+)(?P<mail>[A-Za-z0-9]+([._-][A-Za-z0-9]+)*@[A-Za-z]+(-[A-Za-z]+)*(\.[A-Za-z]+(-[A-Za-z]+)*)+)\b'
text = input()

matches = re.finditer(pattern, text)
for mail in matches:
    print(mail.group('mail'))
