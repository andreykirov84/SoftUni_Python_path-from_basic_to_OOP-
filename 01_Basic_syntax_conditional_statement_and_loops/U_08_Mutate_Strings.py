# """Solution 1 - 60% in judge system"""
# first_string = list(input())
# second_string = list(input())
# result = []
# result_string = ''
# if first_string != second_string:
#     for i in range(len(first_string)):
#         first_string[i] = second_string[i]
#         result_string = ''.join([str(elem) for elem in first_string])
#         if result_string not in result:
#             result.append(result_string)
#             print(result_string)

"""Solution 2 - 100% in judge system - Why???"""
word_1 = input()
word_2 = input()
word_final = ""
prev_word = ""
n = 1

for i in range(len(word_1)):
    word_final += word_2[:n] + word_1[n:]
    n += 1
    if word_final != word_1 and word_final != prev_word:
        print(word_final)
        prev_word = word_final
        word_final = ""
    else:
        word_final = ""
        continue

"""Solution 3 - 60% in judge system"""
# first_string = list(input())
# second_string = list(input())
# result = []
# result_string = ''
#
# for i in range(len(first_string)):
#     first_string[i] = second_string[i]
#     result_string = ''.join([str(elem) for elem in first_string])
#     if result_string not in result:
#         result.append(result_string)
#         print(result_string)
