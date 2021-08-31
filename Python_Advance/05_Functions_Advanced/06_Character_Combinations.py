"""
Variant 1: using ready functions

from itertools import permutations


perm = permutations(input())

for permut in list(perm):
    print(''.join(permut))
"""

# Variant 2: out own function


def print_comb(text, idx):
    if idx >= len(text):
        print(''.join(text))
        return

    for i in range(idx, len(text)):
        text[idx], text[i] = text[i], text[idx]
        print_comb(text, idx + 1)
        text[idx], text[i] = text[i], text[idx]


text = list(input())
print_comb(text, 0)
