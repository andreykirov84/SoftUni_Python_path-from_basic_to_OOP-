# text = 'banana, banana, banana, banana'
# print(text.replace('banana', 'apple'))
# print(text.replace('banana', 'apple', 2))
# print(text[5])
#
# a = ' P34562Z q2576f   H456z'
# print(a.rpartition())


#
# txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.rsplit(", ", 1)
# print(txt.split(", ", 1))
#
# print(x)

a = 'Milk!Pepper!Salt!Water!Banana'
initial_ll = a.split('!')
a_index = initial_ll.index('Pepper')
initial_ll[a_index] = 'Alabala'
print(initial_ll)
