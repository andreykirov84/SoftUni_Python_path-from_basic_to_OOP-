# class A:
#     def __init__(self, number):
#         self.number = number
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         if self.counter == self.number:
#             raise StopIteration
#         else:
#             return self.counter
#
#
# a = A(5)
# for i in a:
#     print(i)    # print 1, 2, 3, 4
#
# print(a.__repr__())
#
# # my_list = [4, 7, 0, 3]
# # # get an iterator using iter()
# # my_iter = iter(my_list)
# # print(next(my_iter))       # 4
# # print(next(my_iter))       # 7
# # print(my_iter.__next__())  # 0
# # print(my_iter.__next__())  # 3
# # next(my_iter)              # Error

def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_first_n = sum(first_n(5))
print(sum_first_n)

