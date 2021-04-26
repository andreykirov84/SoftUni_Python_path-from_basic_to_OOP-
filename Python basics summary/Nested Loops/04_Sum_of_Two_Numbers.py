number_one = int(input())
number_two = int(input())
number_three = int(input())
combinations = 0
result = False
for i in range(number_one, number_two + 1):
    for j in range(number_one, number_two + 1):
        combinations += 1
        if i + j == number_three and not result:
            result = True
            print(f"Combination N:{combinations} ({i} + {j} = {number_three})")
            break
if not result:
    print(f"{combinations} combinations - neither equals {number_three}")
