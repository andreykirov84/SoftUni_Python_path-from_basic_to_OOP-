# def reverse_string(text):   # reverse a string
#     st = []
#     for ch in text:
#         st.append(ch)
#     reversed_text_characters = []
#
#     while st:
#         ch = st.pop()
#         reversed_text_characters.append(ch)
#
#     return ''.join(reversed_text_characters)
#
#
#
#
# # функцията може да се направи и по-просто:
# def reverse_string_simple(text):
#     return text[::-1]
#
# print(reverse_string_simple(input()))

# # Задача 2
# def get_subexpressions(expression):
#     s = []
#     result = []
#     for index in range(len(expression)):
#         ch = expression[index]
#         if ch == '(':
#             s.append(index)
#         elif ch == ')':
#             start_index = s.pop()
#             result.append(expression[start_index:index+1])
#     for i in range(len(result)):
#         print(result[i])
#     return result
#
#
# get_subexpressions("1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5")
# from collections import deque


# def solve():
# #     people = deque()
# #
# #     while True:
# #         command = input()
# #         if command == "End":
# #             print((f'{len(people)} people remaining.'))
# #             break
# #         elif command == "Paid":
# #             while people:
# #                 print((people.popleft()))
# #         else:
# #             people.append(command)
# #
# # solve()

# from collections import deque
#
# def water_dispenser():
#     water = int(input())
#     people = deque()
#     while True:
#         command = input()
#         if command == "Start":
#             break
#         people.append(command)
#
#     while True:
#         command = input().split(' ')
#         if command[0] == "End":
#             break
#         elif command[0] == "refill":
#             water += int(command[1])
#         else:
#             person_water = int(command[0])
#             person = people.popleft()
#             if person_water <= water:
#                 water -= person_water
#                 print(f'{person} got water')
#             else:
#                 print((f'{person} must wait'))
#     print(f'{water} liters left')
# water_dispenser()


from collections import deque
def hot_potato(people, tosses_count):
    people - deque(people)
    index = 0
    while people:
        index += 1
        person = people.popleft()
        if index == tosses_count:
            if people:
                index = 0
                print(f'Removed {person}')

            else:
                print(f'Last is {person}')

        else:
            people.append(person)


hot_potato(input().split(' '), int(input()))
