# class Car:
#     this_is_car_attr = []
#     test_attr = 200
#
#     def __init__(self, model: str, year: int):    # това е метод, защото е в class
#         self.model = model
#         self.year = year
#
#
# car_1 = Car('model7', 1980)
# car_2 = Car('model7', 1980)
# print(car_1.this_is_car_attr)
# print(car_1.test_attr)
# print(car_2.this_is_car_attr)
# print(car_2.test_attr)
# car_1.this_is_car_attr.append(100)
# car_2.this_is_car_attr.append(200)
# car_2.test_attr = 3
#
# print(car_1.this_is_car_attr)
# print(car_1.test_attr)
# print(car_2.this_is_car_attr)
# print(car_2.test_attr)
# print(Car.this_is_car_attr)
# print(Car.test_attr)

#
first_list = [1, 2, 3]
second_list = [4, 5, 6]
print(f' first_list = {first_list}')
print(f' second_list = {second_list}')
first_list.append(10000)
print(f' first_list = {first_list}')
print(f' second_list = {second_list}')
# first_list = second_list
# for i in range(len(second_list)):
#     first_list.append(second_list[i])
first_list = second_list.copy()
print(f' first_list = {first_list}')
print(f' second_list = {second_list}')
second_list.append(55555555)
print(f' first_list = {first_list}')
print(f' second_list = {second_list}')

# a = {1, 2, 3}
# b = {4, 5, 6}
# print(a, b)
# a = b
# print(a, b)
# a.add(10)
# print(a, b)
