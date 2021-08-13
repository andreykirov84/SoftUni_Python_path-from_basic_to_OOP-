# import re
#
# pattern = r'\b[A-Za-z-]+\b'
# text = input().lower()
# target = input().lower()
# words = {}
# matches = re.findall(pattern, text)
#
# for word in matches:
#     if word not in words:
#         words[word] = 1
#     else:
#         words[word] += 1
# if target in words:
#     print(words[target])
# else:
#     print('0')

import re
text = input()
target = input()

pattern = r'(?i)\b' + target + r'\b'

words = {}
matches = re.findall(pattern, text)

print(len(matches))
