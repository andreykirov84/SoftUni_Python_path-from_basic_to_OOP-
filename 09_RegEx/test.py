# import re
# text = 'The rein in Spain'
# x = re.search('\s', text)
# print(x.end())

dd = {'A': 123, 'Bf': 120, 'C': 140, 'Bb': 120}
dd2 = sorted(dd.items(), key=lambda x: (x[1], x[0]))
dd3 = sorted(dd.items(), key=lambda x: (x[1], x[0]), reverse=True)
dd4 = sorted(dd.items(), key=lambda x: (x[1]))
dd5 = dict(dd4)
dd6 = sorted(dd5.items(), key=lambda x: (x[0]))

# print(dd)
# print(*dd.values())
# print(dd2)
# print(dd3)
# print(dd4)
# print(dd5)
# print(dd6)


data = [("Apples", 5, "20"), ("Pears", 1, "5"), ("Oranges", 6, "10")]

data.sort(key=lambda x: x[0])
# print(data)
# OUTPUT
# [('Apples', 5, '20'), ('Oranges', 6, '10'), ('Pears', 1, '5')]

data.sort(key=lambda x: x[1])
# print(data)
# OUTPUT
# [('Pears', 1, '5'), ('Apples', 5, '20'), ('Oranges', 6, '10')]

data.sort(key=lambda x: int(x[2]))
# print(data)
# OUTPUT
# [('Pears', 1, '5'), ('Oranges', 6, '10'), ('Apples', 5, '20')]


# d = {'banana': 3, 'orange': 5, 'apple': 5}
# c = sorted(d.items(), key=lambda x: (-x[1], x[0]))
# print(d)
# print(dict(c))

d = {'banana': 'a', 'orange': 'b', 'apple': 'b'}
c = sorted(d.items(), key=lambda x: (-ord(x[1]), x[0]))
print(d)
print(dict(c))
