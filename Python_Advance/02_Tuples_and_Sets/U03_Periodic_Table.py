elements_set = set()
x = int(input())
for _ in range(x):
    element = input().split(' ')
    for i in range(len(element)):
        elements_set.add(element[i])

element_list = list(elements_set)
for i in range(len(element_list)):
    print(element_list[i])
