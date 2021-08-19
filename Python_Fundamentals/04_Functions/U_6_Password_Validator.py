def pass_validator(password):
    ll = list(password)
    proper_length = False
    only_digits_letters = True
    two_digits = False

    if 6 <= len(ll) < 11:
        proper_length = True

    for i in range(len(ll)):
        if 48 <= ord(ll[i]) <= 57 or 65 <= ord(ll[i]) <= 90 or 97 <= ord(ll[i]) <= 122:
            pass
        else:
            only_digits_letters = False
            break
    n = 0
    for i in range(len(ll)):

        if 48 <= ord(ll[i]) <= 57:
            n += 1
        if n == 2:
            two_digits = True
            break

    return proper_length, only_digits_letters, two_digits


first_rule, second_rule, third_rule = pass_validator(input())

if first_rule and second_rule and third_rule:
    print('Password is valid')
if not first_rule:
    print("Password must be between 6 and 10 characters")
if not second_rule:
    print("Password must consist only of letters and digits")
if not third_rule:
    print("Password must have at least 2 digits")
