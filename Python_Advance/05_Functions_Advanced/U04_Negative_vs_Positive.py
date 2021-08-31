ll = [int(x) for x in input().split(' ')]
positive_ll = [x for x in ll if x >= 0]
negative_ll = [x for x in ll if x < 0]
print(sum(negative_ll))
print(sum(positive_ll))
if abs(sum(negative_ll)) > sum(positive_ll):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")