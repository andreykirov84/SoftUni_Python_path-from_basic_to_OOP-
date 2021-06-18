import re
text = 'The rein in Spain'
x = re.search('\s', text)
print(x.end())
