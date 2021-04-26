number = int(input())
odd_ll = []
even_ll = []
if number > 1:
    for i in range(1, number + 1):
        j = float(input())
        if i % 2 == 0:
            even_ll.append(j)
        else:
            odd_ll.append(j)

    OddSum = sum(odd_ll)
    OddMin = min(odd_ll)
    OddMax = max(odd_ll)
    EvenSum = sum(even_ll)
    EvenMin = min(even_ll)
    EvenMax = max(even_ll)

    print(f"OddSum={OddSum:.2f},")
    print(f"OddMin={OddMin:.2f},")
    print(f"OddMax={OddMax:.2f},")
    print(f"EvenSum={EvenSum:.2f},")
    print(f"EvenMin={EvenMin:.2f},")
    print(f"EvenMax={EvenMax:.2f}")

elif number == 1:
    j = float(input())
    odd_ll.append(j)
    OddSum = odd_ll[0]
    OddMin = odd_ll[0]
    OddMax = odd_ll[0]
    EvenSum = "0.00"
    EvenMin = 'No'
    EvenMax = 'No'
    print(f"OddSum={OddSum:.2f},")
    print(f"OddMin={OddMin:.2f},")
    print(f"OddMax={OddMax:.2f},")
    print(f"EvenSum={EvenSum},")
    print(f"EvenMin={EvenMin},")
    print(f"EvenMax={EvenMax}")

else:
    OddSum = "0.00"
    OddMin = 'No'
    OddMax = 'No'
    EvenSum = "0.00"
    EvenMin = 'No'
    EvenMax = 'No'
    print(f"OddSum={OddSum},")
    print(f"OddMin={OddMin},")
    print(f"OddMax={OddMax},")
    print(f"EvenSum={EvenSum},")
    print(f"EvenMin={EvenMin},")
    print(f"EvenMax={EvenMax}")




