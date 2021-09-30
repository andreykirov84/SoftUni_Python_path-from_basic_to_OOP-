def smallest_number(*args):
    ll = list(args)
    result = min(ll)
    return result


a = int(input())
b = int(input())
c = int(input())
print(smallest_number(a, b, c))
